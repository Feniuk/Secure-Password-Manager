from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import render_template

myDB = SQLAlchemy()

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "my_secret_key "
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///password_manager.db"

    myDB.init_app(app)
    login_manager.init_app(app)

    @app.route("/")
    def landing_page():
        return "Secure Password Manager"

    from app.forms import RegistrationForm
    @app.route("/register", methods=["GET", "POST"])
    def register_user():
        form = RegistrationForm()
        return render_template(
            "registration.html",
            form=form
        )
    return app

@login_manager.user_loader
def login_user(user_id):
    from app.models import User
    return User.query.get(int(user_id))