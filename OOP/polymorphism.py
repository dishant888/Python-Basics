# polymorphism (Many behaviours)

# Operator overloading

# print(3+4)
# print(int.__add__(3,2))

# print('3'+'4')
# print(str.__add__('5','6'))

# print(int.__add__(5,'6')) # Synthetic Sugar
# print(int.__sub__(5,'6')) # Synthetic Sugar

# object + object
class Student:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def get(self):
        print(self.a)
        print(self.b)

    def __add__(self, other): # operator overloading
        obj = Student(self.a + other.a, self.b + other.b)
        return obj

    def __sub__(self, other): # operator overloading
        obj = Student(self.a - other.a, self.b - other.b)
        return obj

    def __str__(self): #  Inbuilt function overloading
        # return f"A, B ={self.a,self.b}"
        return "A = {} \nB = {}".format(self.a,self.b)

obj1 = Student(10,20)
obj2 = Student(100,200)

# obj3 = obj1.__add__(obj2)
#or
obj3 = obj1 + obj2
print(obj3)

obj4 = obj3 - obj2
print(obj4)

#------------------------------------------------------------------------