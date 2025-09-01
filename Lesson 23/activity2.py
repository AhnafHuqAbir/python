s1 = [1, 2, 4, 6, 5, 8]
s2 = [3, 6, 4, 9, 2, 7]
s3 = zip(s1, s2)
print(set(s3))

list1 = [100, 200, 500, 10]
list2 = [10, 50, 20, 90]
rev_list1 = list1[::-1]
for x, y in zip(rev_list1, list2):
    print(x, y)

stoke = ['reliance', 'BMW', 'Tata']
prices = [1000, 5000, 500]

x = {stoke: prices for stoke, prices in zip(stoke, prices)}
print(x)