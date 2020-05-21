# Recursion

#Factorial
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n * fact(n-1)
#
# n = int(input('Enter number: '))
# ans = fact(n)
# print(ans)

#----------------------------------------------------------------------

# Febonacci # 0,1,1,2,3,5,8,13
            # a,b
# def febo(a,b,n):
#     if n == 0:
#         return
#     else:
#         print(a+b,end=',')
#         febo(b,a+b,n-1)
#
# n = int(input('Enter range: '))
# febo(0,1,n)

#----------------------------------------------------------------------

# 1 to 10
# n = 1
# def Myprint():
#     global n
#     if n == 11:
#         return
#     else:
#         print(n)
#         n += 1
#         Myprint()
#
# Myprint()

#----------------------------------------------------------------------

# a = 1000
# print(id(a))
# def update():
#     global a
#     # a = 200
#     print(id(a))
#
# update()
# print(a)

#----------------------------------------------------------------------

# a = 100
# def fun():
#     a = 50
#     x = globals()['a']
#     print(a)
#     print(x)
# fun()

#----------------------------------------------------------------------

# import sys
# sys.setrecursionlimit(200)
#
# print(sys.getrecursionlimit())
# i = 0
# def fun():
#     global i
#     i += 1
#     print('hello : ',i)
#     fun()
# fun()

#----------------------------------------------------------------------