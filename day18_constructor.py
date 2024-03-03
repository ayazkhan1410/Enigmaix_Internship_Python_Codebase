class Calculator:
    # Numbers
    first = 0
    second = 0
  
    # Creating constructors
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def display(self):
        print("First number : " , self.first)
        print("Second number : " , self.second)
    def calculatee(self):
        return self.first + self.second

# Creating an object
cc = Calculator(200,400)
# cc1 = Calculator(1,2)
# displaying and calculating 
cc.display()
aa = cc.calculatee()
print(aa)
# displaying  and calculating for second object
# cc1.display()
# cc1.calculatee()

