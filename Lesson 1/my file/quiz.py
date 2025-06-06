import os

# Color codes
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
    {
        "question": "Who was Player of the Series in the 2025 BPL?",
        "options": ["A. Tamim Iqbal", "B. Liton Das", "C. Mehidy Hasan Miraz", "D. Shakib Al Hasan"],
        "answer": "C"
    },
    {
        "question": "Which country played a Test series in Bangladesh in April 2025?",
        "options": ["A. Zimbabwe", "B. India", "C. Pakistan", "D. Sri Lanka"],
        "answer": "A"
    },
    {
        "question": "When is Bangladesh’s Independence Day celebrated?",
        "options": ["A. 21 February", "B. 16 December", "C. 26 March", "D. 14 April"],
        "answer": "C"
    },
    {
        "question": "What is the name of the Bengali New Year?",
        "options": ["A. Ekushey February", "B. Pohela Boishakh", "C. Bijoy Dibosh", "D. Falgun Mela"],
        "answer": "B"
    },
    {
        "question": "What is the national flower of Bangladesh?",
        "options": ["A. Rose", "B. Water Lily", "C. Jasmine", "D. Lotus"],
        "answer": "B"
    }
]

def start_quiz():
    clear()
    print(f"{CYAN}🇧🇩 Welcome to the Bangladesh 2024–2025 Quiz! 🇧🇩{RESET}\n")
    score = 0

    for idx, q in enumerate(questions, 1):
        print(f"{YELLOW}Q{idx}: {q['question']}{RESET}")
        for option in q['options']:
            print(option)
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        if user_answer == q['answer']:
            print(f"{GREEN}✅ Correct! Well done!{RESET}\n")
            score += 1
        else:
            print(f"{RED}❌ Wrong! Correct answer: {q['answer']}{RESET}\n")

    print(f"{CYAN}🎉 Quiz Complete! 🎉{RESET}")
    print(f"📊 Your final score: {score} / {len(questions)}")

    if score == 15:
        print(f"{GREEN}🌟 You're a Bangladesh expert! Impressive! 🌟{RESET}")
    elif score >= 12:
        print(f"{GREEN}🎯 Great job! You're very informed!{RESET}")
    elif score >= 8:
        print(f"{YELLOW}👍 Not bad! Keep up with the news!{RESET}")
    else:
        print(f"{RED}📘 You need to read more about current events. Try again!{RESET}")

if __name__ == "__main__":
    start_quiz()
