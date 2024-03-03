# There is not public, private and protected concept in python so there is no access modifiers
# But we can use access specifiers in Python

# 1.Public

class Student: 
    def __init__(self):
        self.name = "Ayaz Khan"
        
s = Student()
print(s.name)

# 2. Private 
# For protected specifier we use Doubleundersocre (__)
class Employee:
    def __init__(self):
        self.__cnic = 31101
ee = Employee()
# print(ee.__cnic) we cannot access this like this so what we need to do is
print(ee._Employee__cnic) # This is how we can access private access specifiers in python. This concept is also known as Name mangling

# 3.Protected
# For protected specifier we use single undersocre (_)
# Access only in class and subclasses
class Person:
    def __init__(self):
        self._color = "White"
    def carcolor(self):
        return "Black"
class Ayaz(Person):
    pass

pp = Person()
print(pp._color)
print(pp.carcolor())