#01. Duplicate member check program
def check_duplicate(list1, list2):
    temp1 = set(list1)
    temp2 = set(list2)
    duplicate = temp1.intersection(temp2)
    return duplicate
list1 = []
total = int(input("Enter total number of elements in list1 : "))
for i in range(1,total+1):
    numbers = input(f"Enter number {i} element of the list : ")
    list1.append(numbers)
list2 = []
total2 = int(input("Enter total number of elements in list2: "))
for i in range(1,total2+1):
    numbers2 = input(f"Enter number {i} element of the list : ")
    list2.append(numbers2)

rr = check_duplicate(list1, list2)
if(rr == 0):
    print("No duplicate member found")
else:
    print("Duplicates members are : ", rr)
print("List 1 is : " , list1)
print("List 2 is : " ,list2)

#02. Convert String into number
num1 = int(input("Enter a number to convert into a string")) #100
print(str(num1))
print("Hello world")

#chpt 3 problem 01

def add(num1, num2):
    return f"The sum of {num1} and {num2} are : {num1+num2}"
def subtract(num1, num2):
    return f"The substraction of {num1}, and {num2} are : {num1-num2}"
def multi(num1, num2):
    return f"The multiplication of {num1} and {num2} are : {num1*num2}"
def div(num1, num2):
    return f"The division of {num1} and {num2} are : {num1/num2}"

num1 = float(input("Enter number one : "))
num2 = float(input("Enter number two : "))
operator = input("Enter the operator : ")
if(operator == "+"):
    aa = add(num1,num2)
    print(aa)
elif(operator == "-"):
    ss = subtract(num1,num2)
    print(ss)
elif(operator== "*"):
    mm = multi(num1,num2)
    print(mm)
elif(operator== "/"):
    dd= div(num1, num2)
    print(dd)
else:
    print("Invalid operator ")
    multi(num1,num2)
def add(num1, num2):
    return f"The sum of {num1} and {num2} are : {num1+num2}"
def subtract(num1, num2):
    return f"The substraction of {num1}, and {num2} are : {num1-num2}"
def multi(num1, num2):
    return f"The multiplication of {num1} and {num2} are : {num1*num2}"
def div(num1, num2):
    return f"The division of {num1} and {num2} are : {num1/num2}"

#chp3 problem no 2

def even(number):
    if(number%2==0):
        print(f"Your number {number} is even")
    else:
        print(f"Your number {number} is odd")
number = int(input("Enter the number to check : "))
even(number)

#chp3 problem no 4
def greet(message):
    return f"Hello, {message} how are you doing today?"
message = input("Enter your name : ")
aa = greet(message)
print(aa)

# chp3 problem no 5
def sum_of_squares(numbers):
  sum_of_squares = 0
  for number in numbers:
    sum_of_squares = sum_of_squares + number * 2
  return sum_of_squares
numbers = [1, 2, 3]
print(sum_of_squares(numbers))

#Problem 13
txt = "Hi my name is ayaz khan"
tt= txt.title()
print(tt)
