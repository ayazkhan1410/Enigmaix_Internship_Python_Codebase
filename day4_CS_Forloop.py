#range function
value = range(5)
for i in value:
    print(i, end=',')
'''
#Using a for Loop Without Accessing Items
languages = ["Java", "Python", "Cpp"]
for i in languages:
    print(i)
   
languages = ['Swift', 'Python', 'Go']
for _ in languages:
    print('Hello')
    print('Hi')

# for Loop range
for i in range(10,20,3):
    print(i)
    number1 = float(input("Enter number one : "))
number2 = float(input("Enter number two : "))
print("Press 1 for sum")
print("Press 2 for substraction")
print("Press 3 for mulitiplication")
print("Press 4 for division")
print("Press 5 for floor division")
print("Press 6 for modules")
choice = int(input("Chose the number : "))
if(choice ==1):
    print("The sum of two numbers are : ", number1+number2)
elif(choice==2):
     print("The substraction of two numbers are : ", number1-number2)
elif(choice==3):
      print("The multiplication of two numbers are : ", number1*number2)
elif(choice==4):
      print("The division of two numbers are : ", number1/number2)
elif(choice==5):
      print("The floor division of two numbers are : ", number1//number2)
elif(choice==6):
      print("The moduls of two numbers are : ", number1%number2)
else :
      print("Invalid choice please enter right number")
subject1 = float(input("Enter your first subject marks : "))
subject2 = float(input("Enter your second subject marks : "))
subject3 = float(input("Enter your third subject marks : "))
subject4 = float(input("Enter your fourth subject marks : "))
subject5 = float(input("Enter your fifth subject marks : "))
#subject6 = float(input("Enter your sixth subject marks : "))
avg = ((subject1+subject2+subject3+subject4+subject5))/5
sum = ((subject1+subject2+subject3+subject4+subject5))
print("Your total marks are : ", sum )
if(avg>=90):
 print("You got A+ GRADES")
elif(avg>80 and avg<90):
  print("You got A Grades")
elif(avg>70 and avg<80):
   print("You got B grades")
elif(avg>60 and avg<70):
   print("You got C GRADES")
elif(avg>50 and avg<60):
   print("You got D Grades")
else:
   print("Your fail try next time")
   '''
'''
operators = input("Enter any operator\n")
num1 = float(input("Enter number one\n"))
num2 = float(input("Enter number two \n"))
match operators:
    case '+':
        print("The sum of two numbers are : ", num1+num2)
    case '-':
        print("The difference of two numbers are : ", num1-num2)
    case '*':
        print("The product of two numbers are : ", num1*num2)
    case '/':
        print("The division of two numbers are : ", num1/num2)
    case '%':
        print("The modulus of two numbers are : ", num1%num2)
    case '**':
        print("The exponent of two numbers are : ", num1**num2)
    case _:
        print("Invalid operator")
#For loop
languages = ['Python', 'Java', 'C++', 'Ruby', 'C']
for x in languages:
    print(x, end=',\n')
    for y in x:
        print(y,end=',\n')

# Looping through a string
for x in 'Python':
    print(x, end=',')
    '''