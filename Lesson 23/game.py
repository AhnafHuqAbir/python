print("Welcome to my simple calculator")
want = str(input("Do you want to use it? {yes(y) or no(n)}: ")).lower()
if want == "y":
    print("a.addition")
    print("b.subtraction")
    print("c.Multiplication")
    print("d.division")

    choice = str(input("Enter your choice: ")).lower()
    if choice =="a":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        choose = input("Do you want to add more numbers?{yes(y) or no(n)}: ").lower()
        if choose == "y":
            num3 = int(input("Enter the third number: "))
            num4 = int(input("Enter the forth number: "))
            result = num1 + num2 + num3 + num4
            print(f'the result is {result}')
        else:
            result = num1 + num2
            print(f'the result is {result}')
    if choice =='b':
        num1 = int(input("enter the bigest number: "))
        num2 = int(input("enter the lower number: "))
        result = num1 - num2
        print(f'the result is {result}')