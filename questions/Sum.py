#Sum of n number [1+2+3+4+5..+n]

n = int(input('Enter how many numbers to add: '))

list = []

for i in range(n):
    a = int(input('Enter number: '))
    list.append(a)

def sum(list):
    s = 0
    for i in list:
        s += i
    return s

print(sum(list))
