import os

# Clear screen function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Question data
questions = [
    {
        "question": "What is the capital of Bangladesh?",
        "options": ["A. Chittagong", "B. Dhaka", "C. Sylhet", "D. Khulna"],
        "answer": "B"
    },
    {
        "question": "Who is the national poet of Bangladesh?",
        "options": ["A. Kazi Nazrul Islam", "B. Rabindranath Tagore", "C. Jasimuddin", "D. Shamsur Rahman"],
        "answer": "A"
    },
    {
        "question": "Which river is the longest in Bangladesh?",
        "options": ["A. Jamuna", "B. Teesta", "C. Padma", "D. Meghna"],
        "answer": "C"
    },
    {
        "question": "In which year did Bangladesh gain independence?",
        "options": ["A. 1947", "B. 1952", "C. 1971", "D. 1975"],
        "answer": "C"
    },
    {
        "question": "What is the name of the national flower of Bangladesh?",
        "options": ["A. Water Lily", "B. Rose", "C. Marigold", "D. Jasmine"],
        "answer": "A"
    }
]

# Start quiz
def start_quiz():
    score = 0
    clear()
    print("🇧🇩 Welcome to the Bangladesh Quiz! 🇧🇩\n")

    for idx, q in enumerate(questions, 1):
        print(f"Q{idx}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}\n")

    print(f"🎉 You got {score} out of {len(questions)} correct!")
    if score == len(questions):
        print("🌟 Excellent! You're a true Bangladesh expert!")
    elif score >= 3:
        print("👍 Good job! Keep learning.")
    else:
        print("📘 Study a bit more about Bangladesh!")

# Run it
if __name__ == "__main__":
    start_quiz()
import os

# Clear screen function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Question data
questions = [
    {
        "question": "What is the capital of Bangladesh?",
        "options": ["A. Chittagong", "B. Dhaka", "C. Sylhet", "D. Khulna"],
        "answer": "B"
    },
    {
        "question": "Who is the national poet of Bangladesh?",
        "options": ["A. Kazi Nazrul Islam", "B. Rabindranath Tagore", "C. Jasimuddin", "D. Shamsur Rahman"],
        "answer": "A"
    },
    {
        "question": "Which river is the longest in Bangladesh?",
        "options": ["A. Jamuna", "B. Teesta", "C. Padma", "D. Meghna"],
        "answer": "C"
    },
    {
        "question": "In which year did Bangladesh gain independence?",
        "options": ["A. 1947", "B. 1952", "C. 1971", "D. 1975"],
        "answer": "C"
    },
    {
        "question": "What is the name of the national flower of Bangladesh?",
        "options": ["A. Water Lily", "B. Rose", "C. Marigold", "D. Jasmine"],
        "answer": "A"
    }
]

# Start quiz
def start_quiz():
    score = 0
    clear()
    print("🇧🇩 Welcome to the Bangladesh Quiz! 🇧🇩\n")

    for idx, q in enumerate(questions, 1):
        print(f"Q{idx}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}\n")

    print(f"🎉 You got {score} out of {len(questions)} correct!")
    if score == len(questions):
        print("🌟 Excellent! You're a true Bangladesh expert!")
    elif score >= 3:
        print("👍 Good job! Keep learning.")
    else:
        print("📘 Study a bit more about Bangladesh!")

# Run it
if __name__ == "__main__":
    start_quiz()
import os

# Clear screen function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Question data
questions = [
    {
        "question": "What is the capital of Bangladesh?",
        "options": ["A. Chittagong", "B. Dhaka", "C. Sylhet", "D. Khulna"],
        "answer": "B"
    },
    {
        "question": "Who is the national poet of Bangladesh?",
        "options": ["A. Kazi Nazrul Islam", "B. Rabindranath Tagore", "C. Jasimuddin", "D. Shamsur Rahman"],
        "answer": "A"
    },
    {
        "question": "Which river is the longest in Bangladesh?",
        "options": ["A. Jamuna", "B. Teesta", "C. Padma", "D. Meghna"],
        "answer": "C"
    },
    {
        "question": "In which year did Bangladesh gain independence?",
        "options": ["A. 1947", "B. 1952", "C. 1971", "D. 1975"],
        "answer": "C"
    },
    {
        "question": "What is the name of the national flower of Bangladesh?",
        "options": ["A. Water Lily", "B. Rose", "C. Marigold", "D. Jasmine"],
        "answer": "A"
    }
]

# Start quiz
def start_quiz():
    score = 0
    clear()
    print("🇧🇩 Welcome to the Bangladesh Quiz! 🇧🇩\n")

    for idx, q in enumerate(questions, 1):
        print(f"Q{idx}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}\n")

    print(f"🎉 You got {score} out of {len(questions)} correct!")
    if score == len(questions):
        print("🌟 Excellent! You're a true Bangladesh expert!")
    elif score >= 3:
        print("👍 Good job! Keep learning.")
    else:
        print("📘 Study a bit more about Bangladesh!")

# Run it
if __name__ == "__main__":
    start_quiz()
