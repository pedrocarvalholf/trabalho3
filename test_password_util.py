# test_password_util.py
from password_util import encrypt_password, check_password

def test_encrypt_password():
    password = "senha123"
    hashed_password = encrypt_password(password)
    assert hashed_password is not None

def test_check_password():
    plain_password = "senha123"
    hashed_password = encrypt_password(plain_password)
    assert check_password(plain_password, hashed_password)
    assert not check_password("outrasenha", hashed_password)
