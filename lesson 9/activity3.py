num = int (input("Enter a Number : "))
str_num = str(num)
len_num = len(str_num)
org_num = num
sum = 0

while num > 0:
    digit = num % 10
    digit_cube = digit ** len_num
    sum = sum + digit_cube
    num = num // 10

if (org_num == sum) :
    print(f"{org_num} is an amstrong Number.")
else :
    print(f"{org_num} is not an amstrong Number.")