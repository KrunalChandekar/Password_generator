import secrets
import string

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter the length of the password you want to generate: "))
    password = generate_password(length)
    print("Generated Password:", password)
