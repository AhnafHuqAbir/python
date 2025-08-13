l = [7, 5, 22, 19, 50, 0, 140]

print("Original list:", l)

sum = 0
for i in l:
    sum = sum + i
print("Sum of all elements in the list is ", sum)

length = len(l)
print("the length of the list is ", length)

avg = sum // length
print("Avrage of the list is ", avg)

l.sort()
print("Sorted list:", l)
print("Maximun number", l[0])
print("Minimum number", l[-1]) 
