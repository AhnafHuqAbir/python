seta = {1, 3, 4, 7, 9}
print(seta)

setb = {1, 7.5, "Hellow word", True}
print(setb)

setc = {1, 3, 4, 7, 9, 3, 4, 7}
print("setc =", setc)
listc = list(setc)
print("listc =", listc)

setd = set([2, 6, 8])
print("setd =", setd)

sete = set([0, 1, 2, 5, 6, 7])
print("before poping:", sete)
sete.pop()
print("after poping:", sete)