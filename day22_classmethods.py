class Employee:
    companyname = "Enigmatix"
    def __init__(self, name):
        
        self.name = "Ayaz khan"
    def show(self):
        print(f"Employee name is : {self.name}  and company name is : {self.companyname}")
    @classmethod
    def changeCompany(cls, newcompanyname):
        cls.companyname = newcompanyname
        
# # Creating an object
# ee = Employee("Ayaz")
# # Printing show function
# ee.show()
# # Changing the name of our company
# ee.changeCompany("Nestle")
# Employee.changeCompany("KHAN SPORTS")
# # Now printing show function again
# ee.show()
# # Printing Global variable
# print(Employee.companyname)

class Student:
    marks = 0
    firstname = " "
    lastname = " "
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def show(self):
        print(f"First name is : {self.firstname}")
        print(f"Last name is : {self.lastname}")
        print(f"I got {self.marks}")
    @classmethod
    def clas_method(cls, newmarks): # in cls object we are passing whole class
        Student.marks = newmarks
    @staticmethod
    def check_age():
        age = 0
        if (age<18):
            print("Age is below to 18")
        else:
            print("Age is above to 18")
# Creating object
ss = Student("AYAZ", "KHAN")
# Intilizaing value for class method
Student.marks = 70
ss.show()
# Calling static method
Student.check_age()

# name = "Ayaz  ahmad khan"
# print(name.title())


