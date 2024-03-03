# Types of arguments
# 1. Default argument
# def sum(a=1,b=2):
#     s = a+b
#     print(s)
# sum(b=10) # in default function python automatically detect the function 
# # Now take a look as a String function
# def greet(fname, name1= "Ali", name2 = "Ayaz",name3 = "Abbas"):
#     print("Hello", fname, name1, name2, name3)
# greet("Affan", name3="Imran Khan")

# 2. Keyword arguments
def num(a=1,b=2):
    nu = a*b
    print(nu)
num(b=10, a=2) # The arguments order is not matter

#3. Required arguments
def greet(fname, mname, lname):
    print("Hello", fname, mname, lname)
greet("AYAZ KHAN", "IMRAN KHAN", "ALI KHAN")
# IN REQUIRED ARGUMENTS YOU HAVE TO GIVE ALL THE ARGUMENTS

# 4.Variable length arguments
def sum(*numbers):
    sum = 0
    for i in numbers :
        sum = sum + i
    print("Average is : ", sum/len(numbers))
sum(1,2,3,4,5,6,7,8)

# Return argument
def divv(a,b):
    d = a-b
    return d
print(divv(6,5))
