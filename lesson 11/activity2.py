rows = int(input("Enter your number of rows = "))
number = 1

for i in range(1, rows + 1):
    for h in range(1 , i + 1):
        print( number , end=" ")
        number += 1
    print()