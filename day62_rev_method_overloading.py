class Area:
    def find_area(self,a=None,b=None):
        if a!=None and b!=None:
            print("Area : ", a*b)
        elif a!=None:
            print("Area : ", a*a)
        else:
            print("None")
aa = Area()
aa.find_area()
aa.find_area(10)
aa.find_area(10,12)

def print_digits(number):
    while number > 0:
        digit = number % 10
        print(digit)
        number = number // 10
print_digits(1011)