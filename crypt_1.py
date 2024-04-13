from cryptography.fernet import Fernet
import sqlite3

key = Fernet.generate_key()
cipher = Fernet(key)

conn = sqlite3.connect('credentials.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS credentials (
               id INTEGER PRIMARY KEY AUTO INCREMENT,
               website TEXT NOT NULL,
               username TEXT UNIQUE NOT NULL,
               password TEXT NOT NULL
    )
''')

def encrypt(password):
    encrypted_password = cipher.encrypt(password.encode())
    return encrypted_password.decode()

def decrypt(encrypted_password):
    decrypted_password = cipher.decrypt(encrypted_password)
    return decrypted_password.decode()

def storePassword(website, username, password):
    encrypted_password = (encrypt(password))
    cursor.execute("INSERT INTO credentials (website, username, password) VALUES (?, ?, ?)",
                   (website, username, encrypted_password))
    conn.commit()

def getPasswords(website, username):
    cursor.execute("SELECT password FROM credentials WHERE website=? AND username=?",
              (website, username))
    result = cursor.fetchone()
    if result:
        encrypted_password = result[0]
        decrypted_password = decrypt(encrypted_password)
        return decrypted_password.decode()
    else:
        return None
    
def main():
    storePassword("meow.com", "jordan", "meow")
    retrieved_password = getPassword("meow.com", "jordan")
    print(retrieved_password)

if __name__ == "__main__":
    main()