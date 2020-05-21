
def check(n):
    c = 0
    for i in range(1,n+1):
        if n%i == 0:
            c += 1
    if c == 2:
        return 'Prime'
    else:
        return 'Not prime'

if __name__ == '__main__':
    collection = {}
    for i in range(1,101):
        collection[i] = check(i)
        print(i,':',check(i))
    print(collection)