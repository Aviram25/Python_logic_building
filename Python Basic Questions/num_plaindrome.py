s = 343
n=s
digit = 0
while s != 0:
    temp = s%10
    digit = (digit*10) + temp
    s = s//10

print(digit == n)    