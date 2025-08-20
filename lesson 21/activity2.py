dect = {'codingal' : 2, 'is' : 2, 'best' : 3, 'for' : 2, 'coding' : 1}
k = 2
counter = 0

for key in dect:
    if dect[key] == k:
        counter = counter + 1
print("The number of words with frequency", k, "is", counter)