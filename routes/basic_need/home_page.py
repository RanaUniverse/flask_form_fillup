from flask import (
    Blueprint,
    # request,
    render_template,
    # flash,
)


home_page_blueprint = Blueprint("1st_home_page", __name__)


@home_page_blueprint.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"

    return render_template("index.html")
