class Employee:
    # Creating constructor to set the value
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    # Creating getter
    @property
    def getingeverything(self):
        return self.fname, self.lname, self.salary
    # Creating setters to set the value
    @getingeverything.setter
    def setvalue(self, new_fname, new_lname, new_salary):
        self._fname = new_fname
        self._lname = new_lname
        self._salary = new_salary


ee = Employee("Ayaz", "Khan", 20000)
print(ee.getingeverything)

# setting values
ee.salary =2000
ee.fname = "Ayaz"
ee.lname = "Khan"
print(ee.getingeverything)

# Example 02
# class Shape:
#     length = 0.0
#     width = 0.0
#
#     # Creating getter
#     @property
#     def getlength(self):
#         return self.length * self.width
#     # Creating setter
#     @getlength.setter
#     def setarea(self, length, width):
#         self.length = length
#         self.width = width
# # Creating object
# ss = Shape()
# # Taking input from the user
# ll = float(input("Enter the length : ")) # 4
# ww = float(input("Enter the width : "))
# # Setting the value
# ss.length = ll #4
# ss.width = ww  #5
# # Printing the value
# print(f"The area of rectangle is : {ss.getlength}")

class Student:
    firstname = " "
    lastname = " "
    rollnumber = " "

    @property
    def getvalue(self):
        print(f"First name is {self.firstname}")
        print(f"lAST NAME IS : {self.lastname}")
        print(f"Roll number is : {self.rollnumber}")
    @getvalue.setter
    def setvalue(self,firstname,lastname,rollnumber):
        self.firstname = firstname
        self.lastname = lastname
        self.rollnumber = rollnumber
# Creating object
ss = Student()
ss.firstname = "Ayaz"
ss.lastname = "Khan"
ss.rollnumber = "F20"
aa = ss.getvalue
print(aa)