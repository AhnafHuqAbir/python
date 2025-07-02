word = input("Plz enter your own word : ")
chracter = input("plz enter your own chracter : ")
i = 0
count = 0
while (i < len(word)):
    if(word[i] == chracter):
        count = count + 1    
    i = i + 1

print(f"The total number of times {chracter} has occurred {count}.")