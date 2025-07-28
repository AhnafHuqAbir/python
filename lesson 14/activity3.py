def find_cube(num):
    return num ** 3
def disivible_by_3(num):
    if num % 3 == 0:
        cube = find_cube(num)
        return cube
    else:
        return False
print(disivible_by_3(3))
print(disivible_by_3(27))
print(disivible_by_3(64))
print(disivible_by_3(15))
print(disivible_by_3(12034))