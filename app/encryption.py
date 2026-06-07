import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("SECRET_KEY")

fernet = Fernet(
    key.encode()
)


def encryption(data):
    encrypted = fernet.encrypt(
        data.encode()
    )
    return encrypted.decode()


def decryption(ciphertext):
    decrypted = fernet.decrypt(
        ciphertext.encode()
    )
    return decrypted.decode()