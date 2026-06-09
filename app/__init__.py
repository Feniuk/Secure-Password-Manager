from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import render_template
from flask_login import login_user
from flask_login import logout_user
from flask import redirect
from flask import url_for

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
        return render_template("home.html")


    from app.registration_form import RegistrationForm
    @app.route("/register", methods=["GET", "POST"])
    def register_user():
        form = RegistrationForm()

        if form.validate_on_submit():
            from app.models import User
            from app.security import secure_password
            from app.password_strenght_check import password_strength_check
            from flask import flash

            strenght = password_strength_check(form.password.data)
            if strenght == "Weak":
                flash("Password is too weak")
                return render_template("registration.html",form=form)

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
            flash("User successfully registered!")
            return redirect(url_for("login"))
        
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
                return redirect(
                    url_for("remember_user")
                )
            
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
        return render_template("dashboard.html")
        

    @app.route("/logout")
    @login_required
    def logout():
        from flask import flash
        logout_user()
        flash("Bye bye, hope to see you again!")
        return redirect(url_for("landing_page"))


    @app.route("/store_data", methods=["GET", "POST"])
    @login_required
    def store_data():
        from app.password_storage_form import StorageForm
        from app.models import DataVault
        from app.encryption import encryption
        from flask import flash

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
            
            flash("Data was encrypted and saved.")
            return redirect(url_for("store_data"))
        return render_template(
            "data_to_store.html",
            form=form
        )
    
    @app.route("/retrieve_data")
    @login_required
    def retrieve():
        from app.models import DataVault
        from app.encryption import decryption

        data = DataVault.query.filter_by(
            user_id=current_user.id
        ).all()
        decrypted_entries = []

        for entry in data:
            decrypted_entries.append(
                {
                    "id": entry.id,
                    "website": entry.website,
                    "username": decryption(
                        entry.account_username
                    ),
                    "password": decryption(
                        entry.encrypted_password
                    )
                }
            )
        return render_template(
            "retrieve_data.html",
            entries=decrypted_entries
        )
    
    @app.route("/delete/<int:entry_id>")
    @login_required
    def delete_data(entry_id):
        from app.models import DataVault
        from flask import flash
        data = DataVault.query.get_or_404(
            entry_id
        )
        if data.user_id != current_user.id:
            return "You have no access to delete this data", 403
        myDB.session.delete(data)
        myDB.session.commit()
        flash("Your data was deleted")
        return redirect(url_for("store_data"))
    

    @app.route("/edit/<int:entry_id>", methods=["GET", "POST"])
    @login_required
    def edit_data(entry_id):
        from app.edit import EditForm
        from app.models import DataVault
        from app.encryption import decryption
        from app.encryption import encryption

        entry = DataVault.query.get_or_404(
            entry_id
        )

        if entry.user_id != current_user.id:
            return "You have no access to edit this data", 403
        
        form = EditForm()

        if form.validate_on_submit():
            entry.website = form.website.data
            entry.account_username = encryption(
                form.username.data
            )
            entry.encrypted_password = encryption(
                form.password.data
            )

            myDB.session.commit()
            return redirect(
                url_for("retrieve")
            )

        if not form.is_submitted():
            form.website.data = entry.website
            form.username.data = decryption(
                entry.account_username
            )
            form.password.data = decryption(
                entry.encrypted_password
            )
        return render_template(
            "edit.html",
            form=form
        )
    

    @app.route("/generate_password")
    @login_required
    def pass_gen():
        from app.password_generator import generate_password
        password = generate_password()
        return render_template(
            "generate_password.html",
            password=password
        )
        
    return app


@login_manager.user_loader
def get_user(user_id):
    from app.models import User
    return User.query.get(int(user_id))

