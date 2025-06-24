import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    pwd = ""
    for _ in range(length):
        pwd += random.choice(chars)
    return pwd

try:
    length = int(input("How long do you want your password to be? "))
    if length < 4:
        print("That’s too short. Make it at least 4 characters.")
    else:
        print("Here’s your password:")
        print(generate_password(length))
except:
    print("Oops, that doesn’t look like a number.")
