string = input("Enter a String : ")

print("Derict way to revers string : ", string[::-1])
reversed_string = ""
for letter in string:
    print(letter)
    reversed_string = letter + reversed_string
    print(reversed_string)

print("Reversed string useing for loop : ", reversed_string)