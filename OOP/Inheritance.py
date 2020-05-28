# Inheritance (acquiring properties of another class)

# Single Inheritance

# class parent:
#
#     def fun(self):
#         print('Function of parent class')
#
# class child(parent):
#     def fun2(self):
#         print('Function of child class')
#
# c = child()
# c.fun()
# c.fun2()
#
# p = parent()
# p.fun()

#------------------------------------------------------------------------

# class parent:
#
#     def fun(self):
#         print('Function of parent class')
#
# class child(parent):
#     def fun2(self):
#         print('Function of child class')
#
# c = child()
# c.roll = 101
# c.name = 'Ram'

#------------------------------------------------------------------------

# class parent:
#     a = 100
#     def fun(self):
#         self.b = 200
#         print('Function of parent class')
#
# class child(parent):
#     c = 300
#     a = 1000
#     def fun2(self):
#         self.d = 400
#         # self.a = 2000
#         print('Function of child class')
#
# c = child()
# c.roll = 101
# c.name = 'Ram'
# print(c.a)

#------------------------------------------------------------------------

# Multiple Inheriatnce

# class Teacher1:
#
#     def __init__(self):
#         self.teacher = 'Viajy Sir'
#         self.m = 30
#     def show1(self):
#         print(self.teacher)
#         print(self.m)
#
# class Teacher2:
#     def __init__(self):
#         self.teacher = 'Ajay Sir'
#         self.m = 40
#     def show2(self):
#         print(self.teacher)
#         print(self.m)
#
# class Student1(Teacher1,Teacher2): # acquire and assign value to first class ie Teacher1
#     pass
#
# obj1 = Student1()
# print(obj1.teacher)
#
# class Student2(Teacher2,Teacher1): # acquire and assign value to first class ie Teacher2
#     pass
#
# obj2 = Student2()
# print(obj2.teacher)

#------------------------------------------------------------------------

# Multi Level

# class A:
#     a = 100
#     def showOfA(self):
#         print(self.a)
# class B(A):
#     b = 200
#     def showOfB(self):
#         print(self.b)
# class C(B):
#     c = 300
#     def showOfC(self):
#         print(self.c)
#
# obj = C()
# obj.showOfA()
# obj.showOfB()
# obj.showOfC()
#
# objOfB = B()
# objOfB.showOfA()
# objOfB.showOfB()
#
# objOfA = A()
# objOfA.showOfA()

#------------------------------------------------------------------------