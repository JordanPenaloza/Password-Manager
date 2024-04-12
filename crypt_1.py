import sqlite3
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt():
    password = input("what do you want to encrypt?")
    encrypted_password = cipher.encrypt(password.encode())
    print(encrypted_password.decode())

def decrypt():
    encrypted_password = input("what do you want to decrypt?")
    decrypted_password = cipher.decrypt(encrypted_password)
    print(decrypted_password.decode)

def switch_case(case):
    cases = {
        'encrypt': lambda: encrypt(),
        'decrypt' : lambda: decrypt()
    }
    default_case = lambda: print("Error: Invalid option. Please enter 'encrypt' or 'decrypt'.")
    return cases.get(case, default_case)()

def main():
    case = input("encrypt or decrypt?")
    switch_case(case)



if __name__ == "__main__":
    main()