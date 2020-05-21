#Febonacci 0,1,1,2,3,5,8,13,21 (recursion)

range = int(input('Enter range: '))

def febo(a,b,range):
    if range == 1:
        return 1
    else:
        print(a+b,end=",")
        febo(b,a+b,range-1)

febo(0,1,range)