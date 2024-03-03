# Init method
class Employee:
    name = " "
  #  value = " "
    def __init__(self, name):
        self.name = name
     # str
    def __str__(self):
          return self.name
    # repr 
    def __repr__(self) -> str:
         return f"My name is : {self.name}"
# Creating an obejct
e = Employee("Ayaz")
# Calling str
print(str(e))
# Calling repr
print(repr(e))
