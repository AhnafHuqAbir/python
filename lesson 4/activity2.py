# Write a program to calculate the number of notes in the given amount?

amount = int(input("Enter the amount :"))

note_1000 = amount // 1000
amount %= 1000

# amount % 1000

note_500 = amount // 500
amount %= 500

# amount%500

note_100 = amount // 100
amount %= 100

# amount % 100

note_50 = amount // 50
amount %= 50

# amount % 50

print("1000 notes :", note_1000)
print("500 notes :", note_500)
print("100 notes :", note_100)
print("50 notes :", note_50)