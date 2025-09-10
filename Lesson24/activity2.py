import random

def guess_number():
    num = random.randint(1,10)
    attempts = 0
    print("Guess a number between 1 and 10.")

    while True:
        try:
            Guess = int(input("Enter your number: "))
            attempts += 1
            if Guess < num:
                print("too low!! try again")
            elif Guess > num:
                print("too high!! try again")
            else:
                print(f"Congratulations! You've guessed the number {num} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 10.")
    if input("Do you want to continue? (y/n): ").lower() == 'y':
        guess_number()
guess_number()
