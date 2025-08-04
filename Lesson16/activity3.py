valid = False
while not valid:
    try:
        number = int(input("Enter a number: "))
        if number // 2 == 0:
            print(f"the number is evean : {number}")
        else:
            print(f"the number is odd : {number}")
        valid = True
    except ValueError:
        print("valid Error")