import bcrypt

def secure_password(password):
    bytes_converter = password.encode("utf-8")
    hashed = bcrypt.hashpw(
        bytes_converter,
        bcrypt.gensalt()
    )
    return hashed.decode("utf-8")


def verify_password(password, secure_password):
    return bcrypt.checkpw(
        password.encode("utf-8"),
        secure_password.encode("utf-8")
    )