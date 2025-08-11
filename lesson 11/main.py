print("\n➗ welcome to the simple culculator ➕\n")
print("a. square of a number")
print("b. cube of a number")
print("c. square root of a number")
choice = input("Enter your choice /a/b/c/ : ").lower()

if choice == 'a':
    num = int(input("Enter a number for square: "))
    result = num * num
    print(f'The square of {num} is {result}')
elif choice == 'b':
    number = int(input("Enter a number for cube: "))
    output = number ** 3
    print(f"The result of {number} cubed is {output}")
elif choice =='c':
    value = int(input("Enter a number for square root: "))
    import math
    aftermath = math.sqrt(value)
    print(f'the squre root of {value} is {aftermath}')
else:
    print("Invalid choice. Please select a valid option (a, b, or c).")