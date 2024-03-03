# Example 01
# class Ayaz:
#     backend1 = "Python and Java"
#     def backend(self):
#         print("Backend task implemented using : ", self.backend1)
# class Abbas:
#     frontend1 = "HTM CSS Javascript"
#     def frontend(self):
#         print("Frontend task implemented using : ", self.frontend1)
# class TeamLead(Ayaz,Abbas):
#     def show(self):
#         print("Dynamic website created .... ")
# tt = TeamLead()
# tt.frontend()
# tt.backend()
# tt.show()
# One child class and more than 1 parent classes
# Example 02
# class Employee:
#     name = " "
#     employee_id = 0
#     def __init__(self, name, employee_id):
#         self.name = name
#         self.employee_id = employee_id
#     def show(self):
#         print("Name : ", self.name)
#         print("Id : ", self.employee_id)
# class Manager:
#     department = " "
#     def __init__(self, department):
#         self.department = department
#     def show2(self):
#         print(f"Department : {self.department}")
# class TeamLead(Employee,Manager):
#     experties = " "
#     def __init__(self, name, employee_id, department, experties):
#         self.experties = experties
#         Employee.__init__(self, name, employee_id)
#         Manager.__init__(self,department)
#     def show3(self):
#         print(f"Experties : {self.experties}")
# mm = TeamLead("Ayaz Khan", 12, "IT", "PYTHON")
# mm.show()
# mm.show2()
# mm.show3()
# Example 03
class BackendDevelopers:
    back_end = "Python & Mysql"
    def backend(self):
        print(f"Implementing backend development using : {self.back_end}")
    def show(self):
        print("Hi i am show method of Backend developer class")
class FrontendDevelopers:
    front_end = "HTML, CSS & JAVASCRIPT"
    def frontend(self):
        print(f"Implementing frontend development using {self.front_end}")
    def show(self):
        print("Hi i am show method of frontend developer class")
class TeamLead(FrontendDevelopers,BackendDevelopers):
    def website(self):
        print("Website created successfully ....")
tt = TeamLead()
print("Hello world")

tt.backend()
tt.frontend()
tt.show()
tt.website()
print(TeamLead.mro())