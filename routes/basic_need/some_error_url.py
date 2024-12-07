"""
here i will keep some thigns which is wrong url if user visit this 
funcions and many logics will be in thsi module
"""

from flask import (
    Blueprint,
    # request,
    render_template,
    # flash,
)


error_1_blueprint = Blueprint("my_frst_idea_of_url_wrong", __name__)


@error_1_blueprint.errorhandler(404)
def page_not_found(e: str | None):
    """This is for any get request which is not made in my code"""
    # note that we set the 404 status explicitly
    return render_template("404.html", error_data=e), 404
