import random
import string

# Random Password Generator

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


while True:
    try:
        length = int(input("Enter the length of the password you want: "))
        if length <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")


password = generate_password(length)
print(f"Your random password is: {password}")
