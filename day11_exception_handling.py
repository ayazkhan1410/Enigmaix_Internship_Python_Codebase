#1. Calculating table of the
# try:
#     num1 = int(input("Enter the number to print the table : "))
#     print(f"The multiplication table of {num1} is ")
#     for i in range(1,11):
#         print(f"{num1} X {i} = {num1*i}")
# except:
#     print("Invalid input")
# print("-----------------------")
# print("This is the end of the code")
# print("Thank you for using")
# print("-----------------------")

#2. Checking even or odd numbers
# try:
#     num = int(input("Enter the number : "))
#     if(num %2==0):
#         print("Number is even")
#     else:
#         print("Number is odd")
# except:
#     print("Invalid Input")
# print("-----------------------")
# print("This is the end of the code")
# print("Thank you for using")
# print("-----------------------")

# 3. Numbers divided by zero
# try:
#     num1 = int(input("Enter number one"))
#     num2 = int(input("Enter number two"))
#     res = num1/num2
#     print(f"The Division of {num1} and {num2} is {num1/num2}")
# except ZeroDivisionError:
#     print("0 CANT BE DIVISIBLE")
# print("The program has been terminated successfully")
# print("Thnk you for using our program")

#4. Handling a value error in dict
# dict = {'Physics' : 88, 'English' : 55, 'Computer' : 98, 'Urdu' : 77}
# try:
#     temp = dict.values()
#     print(temp)
# except KeyError(e):
#     print(e)

#5. Learnvern Quiz 
# try:
#     num1 = int(input("Enter number one : "))
#     num2 = int(input("Enter number two : "))
#     if(num1 or num1 == int):
#         print("Number is integer")
# except:
#     print("Number is not integer")

#6. Learnvern Quiz
# try:
#     str1 = input("Enter String : ")
#     if(type(str1) == str):
#         print("Your input is String")
#     else:
#         print("Your input is not a String")
# except:
#     print("The program has been terminated") 

#7. Learnvern Quiz
try:
    num1 = int(input("Enter number one : "))
    num2 = int(input("Enter number one : "))
    if(num1 or num2 == int):
     print("Your numbers are integers ")
except:
    print("Invalid input")
finally:
    print(f"The sum of {num1} and {num2} is : {num1+num2}")
    