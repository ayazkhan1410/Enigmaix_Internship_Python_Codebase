class Interni:
    def __init__(self, name, id, department):
        self.name = name
        self.id = id
        self.department = department
    def disp(self):
        print(f"Name is : {self.name}")
        print(f"Id is : {self.id}")
        print(f"Department is : {self.department}")
class Employee(Interni):
    
   def  disp2(self):
       print("Timing is : 6pm")

# Creating an object
i = Interni("Ayaz",25,"IT")
i.disp()
# Creating an object for employee
ee = Employee("KHAN", 27, "cs")
ee.disp()
ee.disp2() 

class Parent:
    def eyecolor(self):
        print("Eye color is : Black")
    def height(self):
        print("Height is : 5.6 ft")
class Children(Parent):
    def skincolor(self):
        print("Sking color is : Black")
# creating object
cc = Children()
cc.eyecolor()
cc.height()
cc.skincolor()