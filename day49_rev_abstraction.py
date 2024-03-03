import math
from math import pi
class Shape: # Creating abstract class
    def area(self): # Creating abstract method
        pass
class Rectangle(Shape):
    length = 0.0
    width = 0.0
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def display(self):
        print(f"The area of Rectangle is {self.length*self.width}")
class Circle(Shape):
    radius = 0.0
    def __init__(self, radius):
        self.radius = radius
    def display2(self):
        print(f"The area of circle is : {math.pi*self.radius*self.radius}")

# Creating an object
rr = Rectangle(5.2,5.4)
rr.display()

# Creating another object
cc = Circle(3.2)
cc.display2()
# Another example
class StateBANK:
    def interest(self):
        pass
class UBL(StateBANK):
    def interest(self):
        print("UBL Interest rate is : ", 7.6)
class ABL(StateBANK):
    def interest(self):
        print("ABL Interest rate is :", 8.12)
# Creating an object
uu = UBL()
uu.interest()
# Creating another object
aa = ABL()
aa.interest()