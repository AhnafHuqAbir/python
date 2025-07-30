def cheak_result(order):
    if order == "":
        pass
    if order == "exit":
        return "stop"
    if order == "Water":
        print("Sorry, We don't support Water. Skipping.....")
        return
    if order == "spoiled Juice":
        print("Uh-oh, Bad order found - breaking the loop......")
        return
    else:
        print(f"This {order} is a valid order")
while True:
    order = input("Enter your order (or type 'exit' to stop): ")
    result = cheak_result(order)
    if result == "stop":
        print("Exiting the order system. Goodbye!")
        break
    elif result == "Break":
        print("Something went wrong, closing the shop.....")
        break