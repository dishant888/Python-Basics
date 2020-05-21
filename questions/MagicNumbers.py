# 1-1000 magic numbers
#81 = 8+1 = 9 = (palindrome)9*9(real no) = 81
#1729 = 1+7+2+9 = 19 = 91*19 = 1729

for i in range(1,10001):
    n = i
    sum = 0
    reverse = 0
    while n != 0:
        digit = n % 10
        sum += digit
        n //= 10
    save = sum
    while save != 0:
        digit = save % 10
        reverse = reverse * 10 + digit
        save //= 10
    if sum * reverse == i:
        print(i,end=' ')