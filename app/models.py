from app import myDB

class User(myDB.Model):
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