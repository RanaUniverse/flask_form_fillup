from flask import Flask, request, render_template

app = Flask(__name__)


# The main index.html can return the /submit_note_form to fillup form
@app.get("/")
def home_get():
    print("A user just give get req here now")
    return render_template("index.html")


@app.get("/note_form_fillup")
def note_form_page():
    print("A User want to fillup the form")
    return render_template("note_form_fillup.html")


# This below will come when user will do form fillup and then press submit
@app.post("/submit_note_form")
def submit_note_form():
    fullname = request.form.get("fullname")
    phone_no = request.form.get("phone_no")
    gender = request.form.get("gender")
    note_title = request.form.get("note_title")
    note_subject = request.form.get("note_subject")

    return render_template(
        "note_form_submission.html",
        fullname=fullname,
        phone_no=phone_no,
        gender=gender,
        note_title=note_title,
        note_subject=note_subject,
    )


@app.get("/submit_note_form")
def wrong_note_submit():
    # This will execute when user will wrongly refresh or visit the url
    return render_template("note_form_link_get.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999, debug=True)
