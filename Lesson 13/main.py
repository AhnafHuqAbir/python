import os
import time

def shutdown_laptop():
    print("Your laptop will shut down in 10 seconds...")
    time.sleep(3)
    os.system("shutdown /s /t 10")

def cancel_shutdown():
    print("Shutdown cancelled.")
    os.system("shutdown /a")

def main():
    print("==== Shutdown My Laptop ====")
    print("1. Shutdown Now")
    print("2. Cancel Shutdown")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        shutdown_laptop()
    elif choice == '2':
        cancel_shutdown()
    else:
        print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
