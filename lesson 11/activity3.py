rows = int(input("Enter your number of rows : "))

for i in range(rows):
    for x in range(rows - i - 1):
        print(" " , end="")
    for x in range(2 * i + 1):
        print("*", end= "")
    print()

for i in range(rows - 2 , -1 , -1):
    for x in range(rows - i - 1):
        print(" " , end="")
    for x in range(2 * i + 1):
        print("*", end= "")
    print()