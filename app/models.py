from app import myDB
from flask_login import UserMixin

class User(UserMixin, myDB.Model):
    id = myDB.Column(myDB.Integer, primary_key=True)

    username = myDB.Column(
        myDB.String(80),
        unique = True,
        nullable = False
    )

    email = myDB.Column(
        myDB.String(120),
        unique = True,
        nullable=False
    )

    password_hash = myDB.Column(
        myDB.String(255),
        nullable=False
    )

    def __repr__(self):
        return f"<User {self.username}>"
    


class DataVault(myDB.Model):
    website = myDB.Column(
        myDB.String(200),
        nullable=False
    )
    id = myDB.Column(
        myDB.Integer,
        primary_key=True
    )
    account_username = myDB.Column(
        myDB.String(100),
        nullable=False
    )
    encrypted_password = myDB.Column(
        myDB.Text,
        nullable=False
    )
    user_id = myDB.Column(
        myDB.Integer,
        myDB.ForeignKey("user.id"),
        nullable=False
    )
    def __repr__(self):
        return f"<DataVault {self.website}>"