t = (1, 2, 3, 3, 2, 1,)

def if_palindrome(t):
    first_index = 0
    last_index = len(t) - 1

    while first_index < last_index:
        if t[first_index] != t[last_index]:
            return False
        first_index += 1
        last_index -= 1
    return True

if if_palindrome(t):
    print("The tuple is a palindrome")
else:
    print("The tuple is not a palindrome")
