# main.py
from password_util import read_password, check_password

def main():
    user_password = input("Digite a senha: ")
    stored_password = read_password("stored_password.txt")

    if check_password(user_password, stored_password):
        print("Senha correta.")
    else:
        print("Senha incorreta.")

if __name__ == "__main__":
    main()

