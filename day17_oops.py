# Creating a class
class Student: 
    # Creating Attributes of class
    name = ""
    age = 0

# Creating object of our class
Student1 = Student()
Student1.name= "Ayaz"
Student1.age = 17

# Creating more objects of our class
Student2 = Student()
Student2.name = "Khan"
Student2.age = 14

# Printing objects
print(f"The Student name is {Student1.name}, and age is {Student1.age} ")
# Printing object for our class 2
print(f"2nd Student name {Student2.name}, and age is : {Student2.age}")

# Inheritance in python
# Parent class
class Animal:
    def eat(self):
        print("I can eat")
    def walk(self):
        print("I can walk")
# Childern Class
class Dog(Animal):
    def color(self):
        print("Dog color is Red")
    def bark(self):
        print("Dog can bark")

# Creating an object for dog
Dog1 = Dog() 
# Calling member of Parent class
Dog1.eat()
Dog1.walk()
# Calling Member of Child class
Dog1.color()
Dog1.bark()
#Creating an object for Animal
Animal1 = Animal()
print("----- Animal methods ------")
Animal1.eat()
Animal1.walk()

class Vehicle:
    def Speed(self):
        print("Vehcile speed is fast")
    def honk(self):
        print("Honk !! Honk !!")
class CD70(Vehicle):
    def engine(self):
        print("i got 70 mil engine")
    def color(self):
        print("My color is red")
# Creating an object for CD70
cc = CD70()
cc.color()
cc.engine()
cc.honk()
cc.Speed()

class Human:
    def eat(self):
        print("i am eating")
    def run(self):
        print("Person can run")
class Male(Human):
    def color(self):
        print("Male color is black")
# Creating an object 
male1 = Male()
male1.color()

