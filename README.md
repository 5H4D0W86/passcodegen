# passcodegen
password generator
import os
import base64

def generate_password(length):
    """Generates a password of specified length."""
    # Generate random bytes and convert to base64 string
    password = base64.b64encode(os.urandom(48)).decode('utf-8')
    # Truncate to desired length
    return password[:length]

print("This is a simple password generator")

while True:
    pass_length = int(input("Please enter the length of the password: "))

    # Generate 5 passwords
    for _ in range(5):
        print(generate_password(pass_length))

    # Ask the user if they want more passwords
    more = input("Do you need more passwords? y or n: ").strip().lower()

    if more == 'n':
        print("Exiting the password generator. Goodbye!")
        break
