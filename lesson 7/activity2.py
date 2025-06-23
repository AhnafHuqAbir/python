# Write a program to calculate the electricity bill. The bill is calculated by checking the number of units consumed. Suppose the user is consuming less than 50 units. The per-unit cost will be 2.60, and the tax on that bill will be 25. If a user is consuming more than 50 but less than 100. Then the per-unit cost will be 3.25, and the tax on that bill will be 35 If the user is coming more than 100 and less than 200. Then the per-unit cost will be 5.26, and the tax will be 45 And above 200, the cost of the unit is 8.45, and the tax is 75.

unite = int(input("enter the unite consumed : "))

if unite < 50 :
    per_unite_cost = 2.60 * unite
    tex = 25
    total_cost = per_unite_cost + tex
elif unite >= 50 and unite < 100:
    per_unite_cost = 3.25 * unite
    tex = 35
    total_cost = per_unite_cost + tex
elif unite >= 100 and unite < 200:
    per_unite_cost = 5.26 * unite
    tex = 45
    total_cost = per_unite_cost + tex
elif unite >= 200:
    per_unite_cost = 8.45 * unite
    tex = 75
    total_cost = per_unite_cost + tex
else :
    print("please enter the corrent unite consumed!!!")

print("Total Cost : ",round(total_cost,3))