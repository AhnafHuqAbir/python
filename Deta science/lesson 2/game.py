import tkinter as tk
from tkinter import messagebox
import random

#  1. Game Logic Functions

def determine_winner(user_choice, computer_choice):
    """Determines the winner of the round."""
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "User"
    else:
        return "Computer"

def play_game(user_input):
    """Handles the game flow when a button is clicked."""
    global user_score, computer_score

    # Define possible choices
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    # Determine the winner
    winner = determine_winner(user_input, computer_choice)

    # Update labels and score based on the result
    computer_choice_label.config(text=f"Computer chose: {computer_choice.capitalize()}")

    if winner == "User":
        user_score += 1
        result_label.config(text="You Win!", fg="green")
    elif winner == "Computer":
        computer_score += 1
        result_label.config(text="Computer Wins!", fg="red")
    else:
        result_label.config(text="It's a Tie!", fg="blue")

    # Update the score display
    score_label.config(text=f"Score: You {user_score} | Computer {computer_score}")

    # Display the user's choice
    user_choice_label.config(text=f"You chose: {user_input.capitalize()}")

# Initial Scores
user_score = 0
computer_score = 0

# Create the main window
app = tk.Tk()
app.title("Rock Paper Scissors")
app.geometry("400x350")
app.config(bg="#f0f0f0")

# Title and Instructions
title_label = tk.Label(app, text="Rock Paper Scissors", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

instruction_label = tk.Label(app, text="Choose your move:", font=("Helvetica", 12), bg="#f0f0f0")
instruction_label.pack(pady=5)

# Choice Buttons
button_frame = tk.Frame(app, bg="#f0f0f0")
button_frame.pack(pady=10)

# Rock Button
rock_button = tk.Button(button_frame, text="Rock", command=lambda: play_game('rock'), 
                        width=8, bg="#ffcccb", font=("Helvetica", 10, "bold"))
rock_button.grid(row=0, column=0, padx=5)

# Paper Button
paper_button = tk.Button(button_frame, text="Paper", command=lambda: play_game('paper'), 
                         width=8, bg="#b3e5fc", font=("Helvetica", 10, "bold"))
paper_button.grid(row=0, column=1, padx=5)

# Scissors Button
scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play_game('scissors'), 
                           width=8, bg="#c8e6c9", font=("Helvetica", 10, "bold"))
scissors_button.grid(row=0, column=2, padx=5)


#Result Display
user_choice_label = tk.Label(app, text="You chose: None", font=("Helvetica", 11), bg="#f0f0f0")
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(app, text="Computer chose: None", font=("Helvetica", 11), bg="#f0f0f0")
computer_choice_label.pack(pady=5)

result_label = tk.Label(app, text="Make your first move!", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
result_label.pack(pady=10)

#Score Display
score_label = tk.Label(app, text=f"Score: You {user_score} | Computer {computer_score}", 
                       font=("Helvetica", 12), bg="#f0f0f0", fg="#555555")
score_label.pack(pady=10)


# Start the main event loop
app.mainloop()