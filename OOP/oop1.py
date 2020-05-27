# Classes = Template
# object = Instance of class
# DRY = Do not Repeat Yourself

# 1. Basic concepts of OOP
    # 1.1 Class
    # 1.2 Object
    # 1.3 Data Abstractiona and Encapsulation
    # 1.4 Inheritance
    # 1.5 Polymorphism
    # 1.6 Message Passing
    # 1.7 Data Binding

# 2. Python
    # 2.1 Instance Variable: Variables that belong to the Instance (object), different instances can have diff number of Instance Variables
    # 2.2 Instane Method: Methods that are bound to Instance, an Instance is used to call Instance Methods
    # 2.3 self: self is a inbuit pointer that points to the instance (same as this pointer in C), every Instance Method must receive self as argument
    # 2.4 Class Variable: Variable that belongs to class and are shared by all instances
    # 2.5 Class Method: Methods that are bound to Class, class name is used to call Class Methods (since instance is not used for calling, self is not passed as argument, insted cls is passed)
    # 2.6 cls: cls is a pointer that points to the class
    # 2.7 Static Method: Static Methods are bound to a class rather than an object, it just receives arguments and works on them, does not receive any pointers

#------------------------------------------------------------------------

# Defining Class: (Data members and Member functions differ for different objects)

# class Student:
#     pass
#
# Harry = Student()
# Marry = Student()
#
# Harry.name = 'Harry'
# Harry.subjects = ['Maths','English','Physics','Chemistry']
#
# Marry.name = 'Marry'
# Marry.lastName = 'Jones'
#
# print(Harry.name)
# print(Harry.subjects)
# print(Marry.name, Marry.lastName)
# print(Harry.__dict__) # Description of the object
# print(Marry.__dict__) # Description of the object
# print(Marry.__dir__()) # Description of all the properties the object

#------------------------------------------------------------------------

# self is inbuilt pointer which works same as this pointer in C

# class Computer:
#     def display(self): # method
#         print('Display method invoked')
#
# d = Computer()
#
# print(type(d)) # type of d
# d.display()
# #or
# Computer.display(d)

#------------------------------------------------------------------------

# Constructor

# class Demo:
#
#     def __init__(self,name,age,sal): # constructor # name ,age, salary  are instance variable (has to be declared for all objects)
#         self.name = name
#         self.age = age
#         self.sal = sal
#
#     def display(self):
#         print('Name:',self.name)
#         print('Age:',self.age)
#         print('Salary:',self.sal)
#
# obj = Demo('Ram',20,25000)
# obj.display()

#------------------------------------------------------------------------

# Class Variable

# class Employee:
#     numOfLeaves = 8 # class variable (shared by all instances of a class)
#     pass
#
# e1 = Employee()
# e1.numOfLeaves -= 2
# print(e1.numOfLeaves)
#
# e2 = Employee()
# print(e2.numOfLeaves)
#
# print(Employee.numOfLeaves)
# Employee.numOfLeaves = 12
# print(Employee.numOfLeaves)

#------------------------------------------------------------------------

# Class method

# class Student:
#     school = 'MMPS' # class variable (shared by all instances of a class)
#
#     def __init__(self,m1,m2,m3): #instance method (self (object) is used to call instance method)
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#
#     def avg(self): # instance method
#         print(self.m1+self.m2+self.m3/3)
#
#     @classmethod
#     def info(c): # class method (class is used to work on class variable)
#         print(c.school)
#
# s1 = Student(76,73,80)
# # print(Student.school)
# Student.info()
# s1.avg()

#------------------------------------------------------------------------

# Static Method

class Employee:
    numOfLeaves = 8 # class variable (shared by all instances of a class)

    def put(self,name,age,salary): # instance method
        self.name = name
        self.age = age
        self.sal = salary

    def get(self): # instance method
        print(f"Name is {self.name}, Age is {self.age}, Salary is {self.sal}, No of Leaves is {self.numOfLeaves}")

    @classmethod
    def getLeaves(cls):
        return cls.numOfLeaves

    @classmethod
    def updateLeaves(cls, newvalue):
        cls.numOfLeaves = newvalue
        print('Leaves updated to ',newvalue)

    @staticmethod
    def greet():
        print('Inside Greet method (Static)')

e1 = Employee()
e1.put('Rajesh',35,40000)
e1.numOfLeaves = 12
e1.get()
print('Employee Class leaves is ',Employee.getLeaves())
Employee.greet() # greet works for both class and object
e1.greet()