import math

print("a = sin")
print("b = cos")
print("c = tan")
choice = input("choose a/b/c : ").lower()

if choice == 'a':
    sin_value = int(input('Enter a number for sin: '))
    result = math.sin(sin_value)
    print(f'The sine of {sin_value} is {result}')
elif choice == 'b':
    cos_value = int(input('Enter a number for cos: '))
    result = math.cos(cos_value)
    print(f'The cosine of {cos_value} is {result}')
elif choice == 'c':
    tan_value = int(input('Enter a number for tan: '))
    result = math.tan(tan_value)
    print(f'The tangent of {tan_value} is {result}')
else:
    print("Invalid choice. Please choose a, b, or c.")