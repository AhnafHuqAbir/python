def frictional(num):
    if (num == 0) or (num == 1):
        return 1
    
    return num * frictional(num - 1)
print(frictional(5))
print(frictional(19))