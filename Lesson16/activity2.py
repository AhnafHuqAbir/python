try:
    num1 , num2 = eval(input("Enter two numbers separated by a comma: "))
    result = num1 / num2
    print(f"The result is: {result}")
except ZeroDivisionError as z:
    print("Error: Division by zero is not allowed.", z)
except SyntaxError as b:
    print("Please use comma ex: 2,4", b)
except:
    print("Input Error")
else:
    print("No exceptions")
finally:
    print("This will be excuted no matter what !!!")