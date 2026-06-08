import string
import secrets

def generate_password(length=16):
    characters = (
        string.ascii_letters
        + string.digits
        + "!@#$%^&*"
    )
    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )
    return password