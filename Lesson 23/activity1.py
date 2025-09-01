numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda a, b : a + b, numbers1, numbers2)
print(list(result))

number = [1, 2, 4, 5, 7, 8]
def sq(n):
    return n ** 2
sq = map(sq, number)
print(list(sq))