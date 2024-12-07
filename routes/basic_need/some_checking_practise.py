"""
Here is some things for experiment and to use

Currently here is:
linux_logo and /h/somehtig for just fun

"""

from flask import (
    Blueprint,
    url_for,
    # request,
    # render_template,
    # flash,
)


extra_blueprint = Blueprint("A_lot_of_Extra_blueprint", __name__)


@extra_blueprint.route("/h/<name>")
def hello(name: str | None = None):
    return "A Good Things by h"


@extra_blueprint.route("/linux_logo")
def example():
    # Generate a URL for the static file
    return (
        f"The Linux Logo, image URL is: "
        f"{url_for('static', filename='images/icons_logo/linux_logo.png')}"
    )
