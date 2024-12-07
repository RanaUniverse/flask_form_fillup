from flask import (
    Flask,
    render_template,
    url_for,
    # redirect,
    flash,
    request,
    # abort,
)

app = Flask(__name__)
app.secret_key = "dummy_secret_key"  # Required for flash messages


@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"

    return render_template("index.html")


@app.route("/h/<name>")
def hello(name: str | None = None):
    return "A Good Things by h"


@app.route("/linux_logo")
def example():
    # Generate a URL for the static file
    return (
        f"The Linux Logo, image URL is: "
        f"{url_for('static', filename='images/icons_logo/linux_logo.png')}"
    )


@app.errorhandler(404)
def page_not_found(e: str | None):
    """This is for any get request which is not made in my code"""
    # note that we set the 404 status explicitly
    return render_template("404.html", error_data=e), 404


@app.route("/register", methods=["GET"])
def register():
    """
    This will allow the user to show him the form fillup for user
    register form to show him
    """
    return render_template("register_form.html")


@app.route("/register_submit", methods=["POST"])
def register_submit():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    gender = request.form.get("gender")
    button = request.form.get("button")
    print(button)
    print(f"Name: {name}, Email: {email}, Password: {password}")
    flash("Registration successful! Thank you for signing up.")
    # return redirect(url_for("register"))

    gender = request.form.get("gender")

    if gender == "Male":
        gender_message = "Hello, you are a boy. Thanks!"
    elif gender == "Female":
        gender_message = "You are a super Queen!"
    elif gender == "Others":
        gender_message = "You are God-gifted!"
    elif gender == "Hidden":
        gender_message = "You have a hidden personality!"
    else:
        gender_message = "This has not checkied yet"

    # here i used logic inside python not in html
    if button == "create":
        pass  # i want for this it will execute the render template
    elif button == "update":
        return "YOu wanted to update the account"
    elif button == "delete":
        return "YOu want to dele the acccount, i need confirmation"
    else:
        return "There is some problem in the button you pressed"

    return render_template(
        "register_submit.html",
        name_data=name,
        email_data=email,
        password_data=password,
        gender_data=gender,
        gender_message_data=gender_message,
    )


@app.route("/new_note", methods=["GET"])
def new_note():
    """
    This will trigger when user want to make new note
    """
    return render_template("new_note_form.html")    



@app.route("/new_note_submit", methods=["POST"])
def submit_note():
    """
    Handles note submission and displays the details.
    """
    username = request.form.get("username")
    note_title = request.form.get("note_title")
    note_content = request.form.get("note_sub")

    return render_template(
        "new_note_submit.html",
        username=username,
        note_title=note_title,
        note_content=note_content,
    )





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999, debug=True)
