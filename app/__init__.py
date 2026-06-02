from flask import Flask
from flask_sqlalchemy import SQLAlchemy

myDB = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "dev-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///password_manager.db"

    myDB.init_app(app)

    return app