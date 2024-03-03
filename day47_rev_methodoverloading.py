class Person:
    # def show(self):
    #     print("Hi i am show method without Parameter")
    # def show(self, firstname = ''):
    #     print("Hi i am show method with one parameter : ", firstname)
    def show(self, firstname = '', lastname = ''):
        print("Hi i am show method with two parameter : ", firstname, lastname)

pp = Person()
pp.show()
pp.show("Ayaz")
pp.show("ayaz","khan")

# in short we cannot perform method overloading in Python