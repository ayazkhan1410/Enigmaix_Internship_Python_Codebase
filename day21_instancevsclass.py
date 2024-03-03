
class Student:
    # Declaring class variable
    nameofuni = "Islamia university of bahawalpur"
    noofstudents = 0
    def __init__(self, name, rollno, department):
        self.name = name
        self.rollno = rollno
        self.department = department
        if(Student.nameofuni == "Islamia university of bahawalpur"):
         Student.noofstudents += 1
    def show(self):
        print(f" Student name is :  {self.name}, Roll no is {self.rollno}, department is {self.department}, univeristy is {self.nameofuni}, Total students are : {self.noofstudents}") 

# Creating objects
studentname = input("Enter your name : ")
rollno1 = input("Enter your roll number : ")
department1 = input("Enter your department : ")
s = Student(studentname, rollno1,department1)
s.show()
studentname1 = input("Enter your name : ")
rollno2 = input("Enter your roll number : ")
department3 = input("Enter your department : ")
s1 = Student(studentname1, rollno2,department3)
s1.nameofuni = "COMSATS"
s1.show()
    