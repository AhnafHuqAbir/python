def add(P,Q):
    return P + Q
def subtract(P,Q):
    return P - Q
def multiplection(P,Q):
    return P * Q
def divition(P,Q):
    return P / Q

print("Please select options")
print("a.Add")
print("b.Subtract")
print("c.Multiply")
print("d.Divide")

choice = input("Enter your choice (a/b/c/d) = ")

num1 = int(input("Enter the first number = "))
num2 = int(input("enter the second number = "))

if choice == 'a':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == 'b':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == 'c':
    print(f"{num1} * {num2} = {multiplection(num1, num2)}")
elif choice == 'd':
    print(f"{num1} / {num2} = {divition(num1, num2)}")
else:
    print("This is an invalid input")