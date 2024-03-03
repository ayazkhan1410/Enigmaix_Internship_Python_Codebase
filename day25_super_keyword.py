class Student:
    firstname = " "
    lastname = " "
    roll_number = " "
    department = " "
    def __init__(self, firstname, lastname, roll_number, department):
        self.firstname = firstname
        self.lastname = lastname
        self.roll_number = roll_number
        self.department = department
    def show(self):
        print(f"Student name : {self.firstname + self.lastname}")
        print(f"Student department : {self.department}")
        print(f"Student rollNumber : {self.roll_number}")
class Teacher(Student):
    teacherid = " "
    teacher_experties = " "
    def __init__(self, firstname, lastname, roll_number, department, teacherid, teacher_experties):
         super().__init__(firstname, lastname, roll_number, department)
         self.teacherid = teacherid
         self.teacher_experties = teacher_experties
    def show(self):
        print(f"Teacher id : {self.teacherid}")
        print(f"Teacher experties : {self.teacher_experties}")
        return super().show() # THIS WILL RETURN SHOW METHOD OF STUDENT CLASS
# Creating object
# ss = Student("Ayaz", "Khan", "F20", "Information Technology")
# ss.show()
# Creating object for TEACHER
tt = Teacher("Ayaz", "Khan", "F20", "Information Technology", "35", "JAVA + PYTHON")
tt.show()