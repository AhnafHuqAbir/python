a = [1, 4, 7, 9, 12, 15, 18, 20]
b = [i for i in a if i % 2 == 0]
print(b)

c = {c: c ** 2 for c in a}
print(c)