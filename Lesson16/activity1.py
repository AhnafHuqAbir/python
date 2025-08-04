try:
    number = int(input("Enter a number: "))
    print(f"the number is {number}")
except ValueError as exp:
    print("this error is", exp)