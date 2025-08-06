import random
number = random.randint(10,20)

print("I will generate a random number form 10 to 20 . and you will guess it.one digit at a time.")

while True:
    guess = int(input("Enter your best choice: "))
    if guess == number:
        print('your guess is right')
        print(f'the number is {number}')
        break
    else:
        print('your guess is not right . please enter your best choice try again.')