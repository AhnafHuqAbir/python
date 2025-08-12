number = int(input("Enter a decimal number: "))

binary = ""

if number == 0:
    binary ="0"
else:
    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2
print(f"The binary resentation is {binary}")