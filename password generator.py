import random
import string

def generate_password(length):
    # Define possible characters (letters, digits, symbols)
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a password by randomly choosing characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Ask user for desired password length
try:
    user_length = int(input("Enter desired password length: "))
    if user_length < 4:
        print("Password length should be at least 4 characters.")
    else:
        # Generate and display the password
        generated_password = generate_password(user_length)
        print(f"Your generated password is: {generated_password}")
except ValueError:
    print("Please enter a valid number.")
