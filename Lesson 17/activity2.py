import random

options = ["rook", "paper", "scissors"]
user_choice = input('enter your choice : ').lower()
computer_choice = random.choice(options)

print(f'your choice is {user_choice}')
print(f'computer choice is {computer_choice}')

if user_choice == computer_choice:
    print("it is a tie")
elif(user_choice == 'rook' and computer_choice == 'scissors'):
    print("Rook smashes Scissors, you win!!!")
elif(user_choice == "paper" and computer_choice == 'rook'):
    print("Paper covers Rook, you win!!!")
elif(user_choice == 'sissors' and computer_choice == "paper"):
    print("sissors cut paper, you win!!!")
else:
    print("you lose!!!")

    