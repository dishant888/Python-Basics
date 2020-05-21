# 1-1000 strong numbers
# 145 = 1!(1) + 4!(24) + 5!(125) = 145

for i in range(1,1001):
    n = i
    sum = 0
    while n != 0:
        digit = n % 10
        fact = 1
        for j in range(1,digit+1):
            fact *= j
        n //= 10
        sum += fact
    if sum == i:
        print(i,end=' ')