# Write a program to calculate the BMI of a person?

weight = float(input("Enter your weight in kgs : "))
height = float(input("Enter your height in meters : "))

BMI = weight / (height ** 2)
if BMI < 18.5 :
    print("You are under Weight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("You are healthy")
else:
    print("You are over weight")