# Example No 1
# class Animal:
#     def walk(self):
#         print("Hi i am the method of parent class")
# class Dog(Animal):
#     def walk(self):
#         print("Hi i am the method of child class")
# print("Here walk is an override method")
# # Creating an object
# aa = Animal()
# aa.walk()
# dd = Dog()
# dd.walk()
# Example No 2
class Animal:
    def speak(self):
        print("Hi i am an animal")
class Dog(Animal):
    def speak(self):
        print("Woof woof")
    
class Cat(Animal):
    def speak(self):
        print("meow meow")
# Creating an object
aa = Animal()
aa.speak()

dd = Dog()
dd.speak()

cc = Cat()
cc.speak()