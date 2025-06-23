import os
import time

# Colors for styling
GREEN = '\033[92m'
RED = '\033[91m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

questions = [
    {
        "question": "Who was removed from power in Bangladesh in 2024?",
        "options": ["A. Khaleda Zia", "B. Sheikh Hasina", "C. Muhammad Yunus", "D. Shajahan Khan"],
        "answer": "B"
    },
    {
        "question": "Why did mass protests happen in Bangladesh in 2024?",
        "options": ["A. Electricity shortage", "B. Water crisis", "C. Alleged vote rigging & authoritarianism", "D. Fuel price hike"],
        "answer": "C"
    },
    {
        "question": "Who became interim head of government after the 2024 protests?",
        "options": ["A. Dr. Kamal Hossain", "B. Sheikh Hasina", "C. Muhammad Yunus", "D. Mahmudur Rahman"],
        "answer": "C"
    },
    {
        "question": "What major legal action started in 2025 against Sheikh Hasina?",
        "options": ["A. Tax evasion trial", "B. War crimes trial", "C. Terrorism trial", "D. International lawsuit"],
        "answer": "B"
    },
    {
        "question": "What major natural disaster hit Sylhet in 2025?",
        "options": ["A. Earthquake", "B. Wildfire", "C. Flood & Landslides", "D. Cyclone"],
        "answer": "C"
    },
    {
        "question": "What ordinance was amended in 2025 regarding freedom fighters?",
        "options": ["A. Muktijoddha Ordinance", "B. National Freedom Fighters Council Ordinance", "C. Mujib Amar Ordinance", "D. Hero Recognition Law"],
        "answer": "B"
    },
    {
        "question": "What title was removed from Sheikh Mujibur Rahman in the 2025 amendment?",
        "options": ["A. Prime Minister", "B. Father of the Nation", "C. Bangabandhu", "D. National Hero"],
        "answer": "B"
    },
    {
        "question": "What was the 2025 projected GDP growth of Bangladesh?",
        "options": ["A. 5.1%", "B. 4.3%", "C. 6.0%", "D. 3.9%"],
        "answer": "D"
    },
    {
        "question": "What is the name of the huge pro-Palestine protest held in Dhaka in April 2025?",
        "options": ["A. Gaza Rally", "B. March for Gaza", "C. Free Palestine March", "D. Unity for Gaza"],
        "answer": "B"
    },
    {
        "question": "Which team won the 2025 Bangladesh Premier League?",
        "options": ["A. Dhaka Dominators", "B. Fortune Barishal", "C. Sylhet Strikers", "D. Chittagong Kings"],
        "answer": "B"
    },
]

def print_header():
    clear()
    print(f"{CYAN}===== Bangladesh 2024–2025 Quiz Game ====={RESET}\n")

def ask_question(q):
    print(f"{YELLOW}{q['question']}{RESET}")
    for option in q['options']:
        print(option)
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    return answer == q['answer']

def game_over(score):
    print(f"\n{RED}Game Over!{RESET}")
    print(f"Your final score: {score}/{len(questions)}")
    if score == len(questions):
        print(f"{GREEN}Amazing! You got all correct!{RESET}")
    elif score >= len(questions)*0.7:
        print(f"{GREEN}Great job!{RESET}")
    elif score >= len(questions)*0.4:
        print(f"{YELLOW}Good try! Keep learning.{RESET}")
    else:
        print(f"{RED}Better luck next time!{RESET}")

def play_game():
    lives = 4
    score = 0
    asked = 0

    print_header()
    print(f"You have {lives} lives. Each wrong answer loses a life.")
    print("Try to answer all questions correctly!\n")
    input("Press Enter to start...")

    for q in questions:
        clear()
        print_header()
        print(f"Lives: {lives}  |  Score: {score}\n")

        if ask_question(q):
            print(f"{GREEN}Correct!{RESET}")
            score += 1
        else:
            lives -= 1
            print(f"{RED}Wrong! The correct answer was {q['answer']}.{RESET}")
            if lives == 0:
                break
        asked += 1
        time.sleep(1.5)

    game_over(score)

def main():
    while True:
        play_game()
        replay = input("\nDo you want to play again? (Y/N): ").strip().upper()
        if replay != 'Y':
            print(f"{CYAN}Thanks for playing! Goodbye!{RESET}")
            break

if __name__ == "__main__":
    main()

