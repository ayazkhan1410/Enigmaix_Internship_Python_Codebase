# There are two types of polymorphism
# 1. Runtime polymorphism
# (i) Method overloading
# 2. Compiled time polymorpihsm
# (ii) Method overridding
# Lets talk about method overlaoding
# In method overloading class have same name methods but with different arguments
class Calculator:
    a = 0
    b = 0
    def sum(self):
        print("The sum of a is 10")
    def sum(self, a):
        print("The sum of a is : ", self.a)
    def sum(self, a, b):
        print(f"The sum of {self.a} and {self.b} is : {self.a+self.b}")
# Creating an objcet
cc = Calculator()
cc.a = 50
cc.b = 70
# cc.sum() # This is not allowed
# cc.sum(10) # This is not allowed
cc.sum(10,20) # This is allow in Python
# It will give TypeError: Calculator.sum() missing 2 required positional arguments: 'a' and 'b'
#because Python is interpreted language 

# Next we need to talk about method overridding in python
# Rules of method overridding in python are
'''1. Method have same name and also same arguments
2. Inheritance is important part in Method overridding
3. Class must be different in method overridding'''
class Student:
    def rollNumber(self, a):
        print("I am in parent class and my roll number is : F20 with 1 parameter","My number is : ", a)
class Student1(Student):
    def rollNumber(self, b):
        print("Hi I am a child class of Student and my roll number is F30", "My number is : ", b)
        return super().rollNumber(b)
class Student2(Student1):
    def rollNumber(self, c):
        print("Hi i a Child member of Student1 class my roll number is F40", "My number is : ", c)
        return super().rollNumber(c)
#Creating an object of Student2
ss = Student2()
ss.rollNumber(30)

# Spilit method
# scentence = "Hi my name is ayaz khan"
# result = " "
# result = scentence.split(result)
# print(result)