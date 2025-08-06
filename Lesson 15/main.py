try:
    age = int(input("Enter your age: "))

    if age <= 0:
        print("Invalid age: Age must be a positive number.")
    elif age > 120:
        print("Invalid age: Age is unrealistically high.")
    else:
        print("Age is valid.")

        if age % 2 == 0:
            print(f"{age} is Even.")
        else:
            print(f"{age} is Odd.")

except ValueError:
    print("Error: Please enter a valid number for age.")
