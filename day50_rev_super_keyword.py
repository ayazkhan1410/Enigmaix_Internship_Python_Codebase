class Employee:
    name = " "
    id = " "
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def show(self):
        print(f"Name is {self.name} and id is {self.id}")
class Programmer(Employee):
    language = " "
    def __init__(self,name,id,lang):
        self.language = lang
        super().__init__(name,id) # calling super class constructor
    def childshow(self):
        super().show() # calling super class method
        print(f"{self.name} programming langauge is : {self.language}")
# Creating an object
Ali = Employee("Ali Khan", "232")
Ali.show()
# Creating another object
Ayaz = Programmer("Ayaz Khan", "231", "Java")
Ayaz.childshow()