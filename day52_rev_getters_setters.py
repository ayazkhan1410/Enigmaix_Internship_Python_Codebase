import math
from math import pi
# Example No 1
class Circle:
    radius = 0.00
    @property
    def getvalue(self):
        return math.pi * self.radius * self.radius
    @getvalue.setter
    def setvalue(self,radius):
        self.radius = radius
# Creating an object
cc = Circle()
rad = float(input("Enter the radius : "))
# Setting the value
cc.radius = rad
# Getting the value
result = cc.getvalue
print(f"The area of Circle is : {result}")

# Example No 2
class Person:
    name = " "
    phone_number = 0
    @property
    def getvalue(self):
        return self.name, self.phone_number
    @getvalue.setter
    def setvalue(self,name,phone_no):
        self.name = name
        self.phone_number = phone_no
# # Creating an object
# pp = Person()
# # setting the value
# pp.name = "Ayaz"
# pp.phone_number = 231
# # getting the value
# result = pp.getvalue
# print(f"{result}")
# print(type(result))


