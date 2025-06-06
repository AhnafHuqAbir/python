# Write a program to calculate the BMI of a person?
input("Enter your name : ")
weight = float(input("Enter your weight in kgs : "))
height = float(input("Enter your height in feet : "))
height_two = height * 0.3048

BMI = weight / (height_two ** 2)
if BMI < 18.5 :
    print("You are under Weight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("You are healthy")
else:
    print("You are over weight")