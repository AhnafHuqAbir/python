import array as arr

array_num = arr.array('i', [1, 6, 12, 15, 18, 21, 20, 20, 20])
print("original array:", array_num)

for i in array_num:
    print(i)

print("20 occurs", array_num.count(20), "times")

array_num.reverse()
print("reversed array:", array_num)

