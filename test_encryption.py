from app.encryption import encryption
from app.encryption import decryption

text = "misha@gmail.com"

encrypted = encryption(text)

print("Encrypted:")
print(encrypted)

decrypted = decryption(encrypted)

print("\nDecrypted:")
print(decrypted)