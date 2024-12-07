from flask import (
    Blueprint,
    request,
    render_template,
    flash,
)

new_user_register_blueprint = Blueprint("user_register", __name__)


@new_user_register_blueprint.route("/register", methods=["GET"])
def register():
    """
    This will allow the user to show him the form fillup for user
    register form to show him
    """
    return render_template("register_form.html")


@new_user_register_blueprint.route("/register_submit", methods=["POST"])
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
