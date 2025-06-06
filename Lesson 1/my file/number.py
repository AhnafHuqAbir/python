import random

def guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts+1}/{max_attempts}. Your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess == number:
            print(f"🎉 Congratulations! You guessed the number {number} correctly in {attempts} attempts.")
            break
        elif guess < number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

    else:
        print(f"Sorry, you ran out of attempts. The number was {number}.")

    print("Game Over!")

if __name__ == "__main__":
    guessing_game()