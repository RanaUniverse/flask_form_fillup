from flask import (
    Flask,
    # render_template,
    # url_for,
    # redirect,
    # request,
    # abort,
)


from routes.register_related.new_user import new_user_register_blueprint
from routes.note_related.new_note import new_note_blueprint
from routes.basic_need.home_page import home_page_blueprint
from routes.basic_need.some_error_url import error_1_blueprint
from routes.basic_need.some_checking_practise import extra_blueprint

app = Flask(__name__)
app.secret_key = "dummy_secret_key"  # Required for flash messages


app.register_blueprint(new_user_register_blueprint)
app.register_blueprint(new_note_blueprint)
app.register_blueprint(home_page_blueprint)
app.register_blueprint(error_1_blueprint)
app.register_blueprint(extra_blueprint)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999, debug=True)
