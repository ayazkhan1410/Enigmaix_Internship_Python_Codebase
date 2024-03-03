class Animal:
    def eat(self):
        print("I can Eat")
    def drink(self):
        print("I can drink")
class Cat(Animal):
    def mewmew(self):
        print("meoew meoew")
    def skincolor(self):
        print("White")
# Creating object for Animal class
a = Animal()
a.eat()
a.drink()
# Creating object for Cat class
print("*** Cat class ***")
c = Cat()
c.eat()
c.drink()
c.drink()