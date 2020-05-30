# polymorphism (Many behaviours)

# Operator overloading

# print(3+4)
# print(int.__add__(3,2))

# print('3'+'4')
# print(str.__add__('5','6'))

# print(int.__add__(5,'6')) # Synthetic Sugar
# print(int.__sub__(5,'6')) # Synthetic Sugar

# object + object

# class Student:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def get(self):
#         print(self.a)
#         print(self.b)
#
#     def __add__(self, other): # operator overloading
#         obj = Student(self.a + other.a, self.b + other.b)
#         return obj
#
#     def __sub__(self, other): # operator overloading
#         obj = Student(self.a - other.a, self.b - other.b)
#         return obj
#
#     def __str__(self): #  Inbuilt function overloading
#         # return f"A, B ={self.a,self.b}"
#         return "A = {} \nB = {}".format(self.a,self.b)
#
# obj1 = Student(10,20)
# obj2 = Student(100,200)
#
# # obj3 = obj1.__add__(obj2)
# #or
# obj3 = obj1 + obj2
# print('OBJ 3: ',obj3)
#
# obj4 = obj3 - obj2
# print('OBJ 4: ',obj4)

#------------------------------------------------------------------------

# Function Overloading

# class Student:
#
#     def sum(self,a = None,b = None, c = None):
#         if a != None and b != None and c != None:
#             return a+b+c
#         elif a != None and b != None:
#             return a+b
#         else:
#             return a
#
# obj = Student()
# print(obj.sum(1,2,3))
# print(obj.sum(1,2))
# print(obj.sum(1))


# class Student:
#
#     def sum(self,*a):
#         s = 0
#         for i in a:
#             s += i
#         return s
#
# obj = Student()
# print(obj.sum(1,2,3,4,5))
# print(obj.sum(1,4))
# print(obj.sum(1))

#------------------------------------------------------------------------

# Overriding

# class P1:
#     classVar = 'Class Variable P1'
#     def show(self):
#         self.classVar = 'Instance Variable P1'
#         print('Show of P1')
#
# class P2(P1):
#     classVar = 'Class Variable P2'
#     def show(self):
#         self.classVar = 'Instance Variable P2'
#         print('Show of P2')
#     # pass
#     # def show(self):
#     #     print('Show of P2')
#
# obj = P2()
# obj.show()
# print(P2.classVar) # Calls Class Var of P2 class
# print(obj.classVar) # Calls Instance Var of obj

#------------------------------------------------------------------------

# class A:
#
#     classVar = 'Class Variable A'
#
#     def __init__(self):
#         self.classVar = 'Instance Variable A'
#         self.someVar = 'Some Instance Variable A'
#         self.someVar2 = 'Some Instance Variable 2 A'
#
#     def ShowOFA(self):
#         print('Class A')
#
# class B(A):
#
#     classVar = 'Class Variable B'
#
#     def __init__(self):
#         super().__init__()
#         super().ShowOFA()
#         self.classVar = 'Instance Variable B'
#         self.someVar = 'Some Instance Variable B'
#         # super().__init__() # this will override self.someVar of B with A
#         # super().ShowOFA()
#         # super() is used to point to parent class
#
# objOfA = A()
# objOfB = B()
#
# print(objOfB.someVar)
# print(objOfB.classVar)
# print(objOfB.someVar2)

#------------------------------------------------------------------------