print("Wellcome to my simple culculator")

print("a. Add")
print("b.subtraction")
print("c. Multiply")
print("d. Divide")

choose = input("Enter your choice (a/b/c/d): ")

if choose == "a":
    num1 = int(input("Enter the first Number: "))
    num2 = int(input("Enter the second Number: "))
    result = num1 + num2
    print("The result is: ", result)

elif choose == "b":
    num1 = int(input("Enter the first Number: "))
    num2 = int(input("Enter the second Number: "))
    result = num1 - num2
    print("The result is: ", result)

elif choose == "c":
    num1 = int(input("Enter the first Number: "))
    num2 = int(input("Enter the second Number: "))
    result = num1 * num2
    print("The result is: ", result)

elif choose == "d":
    num1 = int(input("Enter the first Number: "))
    num2 = int(input("Enter the second Number: "))
    result = num1 / num2
    print("The result is: ", result)