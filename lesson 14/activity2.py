def total_calc(bill_amount , tip_perc):
    total = bill_amount + (bill_amount * tip_perc) // 100
    print(total)
total_calc(130, 20)