# Count characters in a number using while loop

number = input("Enter a number: ")

count = 0
index = 0

while index < len(number):
    count += 1
    index += 1

print(f"The number you entered has {count} characters.")
