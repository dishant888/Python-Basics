# 1-1000 Armstrong Numbers
# 153 = 1**3(3) + 5**3(125) + 3**3(27)

for i in range(1,1001):
    n = i
    sum = 0
    while n != 0:
        digit = n % 10
        sum += digit ** 3
        n //= 10
    if sum == i:
        print(i,end=' ')