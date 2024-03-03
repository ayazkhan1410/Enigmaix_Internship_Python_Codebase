import math
i = True
while(i):
    num1 = float(input("Enter number one : "))
    num2 = float(input("Enter number two : "))
    print("Press 1 for sum")
    print("Pres 2 for substraction")
    print("Pres 3 for division")
    print("Pres 4 for multiplication")
    choice = int(input("Choose one number : "))
    # Creating functions
    def sumcal(a,b):
        sum = a+b
        print(sum)
    def sub(a,b):
        sub1 = a-b
        print(sub1)
    def div(a,b):
        div1 = math.floor(a/b)
        print(div1)
    def multi(a,b):
        mul = a*b
        print(mul)
 # using if else 
    if(choice ==1):
        sumcal(num1,num2)
    elif(choice ==2):
        sub(num1,num2)
    elif(choice == 3):
        div(num1, num2)
    elif(choice==4):
        multi(num1, num2)
    else :
        print("Inavlid choice")
    user_input = input("Do you want to continue? y/n : ")
    if(user_input.lower() == "y"):
        i = True
    else:
        i = False
        print("Thank you for using our calculator")