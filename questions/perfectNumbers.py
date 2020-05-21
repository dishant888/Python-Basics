# 1-1000 perfect number
# 6 = 1+2+3 = 6

for i in range(1,1001):
    sum = 0
    for j in range(1,i):
        if i%j == 0:
            sum += j

    if sum == i:
        print(i,end=' ')