from flask import (
    Blueprint,
    request,
    render_template,
)


new_note_blueprint = Blueprint("new_note_related_things", __name__)


@new_note_blueprint.route("/new_note", methods=["GET"])
def new_note():
    """
    This will trigger when user want to make new note
    """
    return render_template("new_note_form.html")


@new_note_blueprint.route("/new_note_submit", methods=["POST"])
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
