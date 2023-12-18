# password_util.py
import hashlib

def read_password(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def encrypt_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def check_password(plain_password, hashed_password):
    return encrypt_password(plain_password) == hashed_password
