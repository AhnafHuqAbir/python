customer_name = input("Customer name: ")
given_amount = float(input("Amount given by customer (in Taka): "))
bill_amount = float(input("Bill amount (in Taka): "))

if given_amount > bill_amount:
    due = 0
    extra = given_amount - bill_amount
    print(f"\n{customer_name} gave extra {extra} Taka. No due.")
elif given_amount == bill_amount:
    due = 0
    print(f"\n{customer_name} paid the bill exactly. No due.")
else:
    due = bill_amount - given_amount
    print(f"\n{customer_name} still owes {due} Taka.")

print("\n--- Summary ---")
print(f"Customer Name: {customer_name}")
print(f"Amount Given : {given_amount} Taka")
print(f"Bill Amount  : {bill_amount} Taka")
if due > 0:
    print(f"Due Amount   : {due} Taka (to be paid later)")
else:
    print("Deu Amount  : 0 Taka (No due)")



# https://gifft.me/o/hw/9ve7n88s68elg3al4b1ds32l