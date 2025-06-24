# Write a program to select a ride according to your preference. The ride is divided into two major categories: 1. Bike 2. Car And further, bikes and cars are divided into 2 subcategories. To give the user better selection options.

print("Select your ride")
print("1. bike")
print("2. car")

choice = int(input("Enter your choice : "))

if choice == 1:
    print("What type of bike : ")
    print("1.Scooty \n")
    print("2.Scooter \n")
    choice2 = int(input("Enter your choice : "))
    if choice2 == 1:
     print("you have selected scooty")
    elif choice2 == 2:
       print("you have selected scooter")
    else :
       print("please choice some of them 1 or 2")
elif choice == 2:
    print("what type of car : ")
    print("1.Sedan")
    print("2.xuv") 
    choice3 = int(input("Enter your choice 1 or 2 : "))
    if choice3 == 1:
        print("you have choiced sedan")
    elif choice3 == 2:
       print("you have choiced XUV")
    else :
       print("Enter your choice 1 or 2") 