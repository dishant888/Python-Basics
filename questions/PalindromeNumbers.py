# 1-1000 palindrome numbers:
# 989 = 989
for i in range(1,1001):
    n = i
    reverse = 0
    while n != 0:
        digit = n % 10
        reverse = (reverse * 10) + digit
        n //= 10
    if i == reverse:
        print(i,end=' ')