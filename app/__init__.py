from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import render_template
from flask_login import login_user
from flask_login import logout_user

myDB = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = "login"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "my_secret_key "
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///password_manager.db"

    myDB.init_app(app)
    login_manager.init_app(app)

    @app.route("/")
    def landing_page():
        return "My Secure Password Manager"


    from app.registration_form import RegistrationForm
    @app.route("/register", methods=["GET", "POST"])
    def register_user():
        form = RegistrationForm()

        if form.validate_on_submit():
            from app.models import User
            from app.security import secure_password

            hashed_password = secure_password(
                form.password.data
            )
            new_user = User(
                username=form.username.data,
                email=form.email.data,
                password_hash=hashed_password
            )
            
            myDB.session.add(new_user)
            myDB.session.commit()
            return "User successfully registered!"
        
        return render_template(
            "registration.html",
            form=form
        )
    
    @app.route("/login", methods=["GET", "POST"])
    def login():
        from app.login_form import LoginForm
        from app.models import User
        from app.security import verify_password
        from flask_login import login_user

        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(
                username=form.username.data
            ).first()
            if user and verify_password(
                form.password.data,
                user.password_hash
            ):
                login_user(user)
                return "Login successful!"
            
            return "Wrong username or password"
        return render_template(
            "login.html",
            form=form
        )
    
    from flask_login import login_required
    from flask_login import current_user
    @app.route("/dashboard")
    @login_required
    def remember_user():
        return f"Welcome my dear {current_user.username}!"
        

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        return "Bye bye, hope to see you again!"


    @app.route("/store_data", methods=["GET", "POST"])
    @login_required
    def store_data():
        from app.password_storage_form import StorageForm
        from app.models import DataVault
        from app.encryption import encryption

        form = StorageForm()

        if form.validate_on_submit():
            encrypted_username = encryption(
                form.username.data
            )
            encrypted_password = encryption(
                form.password.data
            )
            entered_data = DataVault(
                website=form.website.data,
                account_username=encrypted_username,
                encrypted_password=encrypted_password,
                user_id=current_user.id
            )

            myDB.session.add(entered_data)
            myDB.session.commit()
            return "Data was encrypted and saved."
        return render_template(
            "data_to_store.html",
            form=form
        )

    return app


@login_manager.user_loader
def get_user(user_id):
    from app.models import User
    return User.query.get(int(user_id))

