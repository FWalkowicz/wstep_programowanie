import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def encryption(passwd):
    password_provided = passwd  # <- klucz do odszywrowania plików, jeżeli wprowadze złe hasło to plik nie odszyfruje się poprawnie
    password = password_provided.encode()  # <- szyfrowanie
    salt = b'\xe1\xfc#\x9f\x14o\xc9\xea\xce\xdf\x1f\xc60k\x03\xfe'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once
    print(key)
