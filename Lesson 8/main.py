number = int(input("Write a number that you would multiply this number by several times(only write the number) : "))
n = int(input("How many times will you multiply that number(write only the number): "))

power = 1
for x in range(1, n+1):
    power *= number

print(power)