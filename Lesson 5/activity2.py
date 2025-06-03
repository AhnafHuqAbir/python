# Write to check if a person is buying oranges at 100 taka and later selling it 1at 120 taka. Find that he has profit or loss?

buying_price = 100
selling_price = 120

if buying_price < selling_price:
    profit = selling_price - buying_price
    print("It is a profit of", profit ,"taka")
else:
    loss = buying_price - selling_price
    print("It is loss of", loss, "taka")