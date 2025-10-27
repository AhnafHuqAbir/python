print("Hi. Welcome to my math quiz!!!")
print("you will get 4 qustions each qustion you get 5 points. if you got 15 points you win otherwise you lose")
value = input("Are you ready to play (yes(y) or no(n))? : ").lower()
score = 0
if value == 'y':
    print("1. what is the Area of a square ")
    answer = "side * length"
    user_answer = input("Enter your answer: ")
    if user_answer == answer:
        score += 5
        print(f"correct.Now your score is {score} \n")
    else:
        print(f"wrong answer.the correct answer is {answer} \n")

    print("2. what is the formula of Pithagorean theorem")
    answer = "a^2 + b^2 = c^2"
    user_answer = input("Enter your answer: ")
    if user_answer == answer:
        score += 5
        print(f"correct.Now your score is {score} \n")
    else:
        print(f"wrong answer.the correct answer is {answer} \n")
    
    print('3. what is the answer of 8/4/2')
    answer = "1"
    user_answer = int(input("Enter your answer in integer: "))
    if user_answer == int(answer):
        score += 5
        print(f"correct.Now your score is {score} \n")
    else:
        print(f"wrong answer.the correct answer is {answer} \n")

    print("4. what is the answer of 2*2*2*2")
    answer = "16"
    user_answer = input("Enter your answer: ")
    if user_answer == answer:
        score += 5
        print(f"correct.Now your score is {score} \n")
    else:
        print(f"wrong answer.the correct answer is {answer} \n")
    
    if score >= 15:
        print(f"congratulations you win the game.your score is {score}")
    else:
        print(f"Ha...Ha...Ha__you lose the game. You are loser.your score is {score} ^_^")

elif value == 'n':
    print("Ha__ha..edit.bye")
