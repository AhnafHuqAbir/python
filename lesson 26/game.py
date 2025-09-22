print("\n welcome to my simple calculator")
print("a.addition")
print("b.subtraction")
print("c.Multiplecation")
print("d.division")
print("e.esquare")
print("f.cube")

choice = str(input("Enter your choice: ")).lower()
if choice == "a":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    choose = input("Do you want to add more numbers?{yes(y) or no(n)}: ").lower()
    if choice == "y":
        num3 = int(input("Enter the third number: "))
        num4 = int(input("Enter the forth number: "))
        result = num1 + num2 + num3 + num4
        print(f'the result is {result}')
    else:
        result = num1 + num2
        print(f'the result is {result}')
elif choice == "b":
    num1 = int(input("enter the bigest number: "))
    num2 = int(input("enter the lower number: "))
    result = num1 - num2
    print(f'the result is {result}')
elif choice == "c":
    num1 = int(input("enter the first number: "))
    num2 = int(input("enter the second number: "))
    if choice == "y":
        num3 = int(input("Enter the third number: "))
        num4 = int(input("Enter the forth number: "))
        result = num1 * num2 * num3 * num4
        print(f'the result is {result}')
    else:
        result = num1 * num2
        print(f'the result is {result}')
elif choice == "d":
    num1 = int(input("enter the bigest number: "))
    num2 = int(input("enter the lower number: "))
    result = num1 // num2
    print(f'the result is {result}')
elif choice == "e":
    num1 = int(input("enter the number: "))
    result = num1 ** 2
    print(f'the result is {result}')
elif choice == "f":
    num1 = int(input("enter the number: "))
    result = num1 ** 3
    print(f'the result is {result}')
elif ValueError:
    print("invalid input")
else:
    print("invalid input")