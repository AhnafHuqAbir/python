print("a = C°")
print("b = F°")

choice = input("Chose a/b : ")
if choice == "a":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is {fahrenheit}°F")
    if ValueError:
        print("Invalid input. Please enter a valid temperature.")
    else:
        print("Conversion successful!")
elif choice == 'b':
    fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f'{fahrenheit}°F is {celsius}°C')
    if ValueError:
        print("Invalid input. Please enter a valid temperature.")
    else:
        print("Conversion successful!")
elif ValueError:
    print("Invalid input. Please enter a valid temperature.")
else:
    print("Invalid choice. Please choose 'a' or 'b'.")
print("Thank you for using the temperature converter!")