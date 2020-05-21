#Factorial

# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     return fact
#
# n = int(input())
# print(factorial(n))

## or with recursion

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input())
print(factorial(n))