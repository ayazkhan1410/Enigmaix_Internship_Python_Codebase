# try:
#     user_Input = int(input("Enter any number : "))
#     print(user_Input + 4)
# except Exception as e:
#     print("Some error occurred : ", e)

# Second example
# try:
#     even_numbers = [2,4,6,8]
#     print(even_numbers[5])
# except IndexError:
#     print("Index out of bound")
# except:
#     print("Some error occurred")

# Third example
# try:
#     num1 = int(input("Enter num1 :"))
#     num2 = int(input("Enter num1 :"))
#     result = num1/num2
#     print(f"The division of {num1} and {num2} is : {result}")
# except ZeroDivisionError:
#     print("Cannot divided with zero")
# except Exception as e:
#     print("Please enter valid input", e)
# finally:
#     print("The program has been terminated")

# Writing own exception
# class InvalidAgeException(Exception):
#     "Raised when the input value is less than 18"
#     pass
# try:
#     age = 77
#     if age < 18:
#         raise InvalidAgeException
#     else:
#         print("You can vote")
# except InvalidAgeException:
#     print("Exception occurred: Invalid Age")
# finally:
#     print("Thanks for using our program")

# class MyException(Exception):
#     pass
# age = 25
# if age>30:
#     raise MyException("Age is greater than 30")
# else:
#     print("Age is less")

# Exercise
# Problem no 1
# try:
#     num1 = int(input("Enter number one : "))
#     num2 = int(input("Enter number two : "))
#     if type(num1 and type(num2) == int):
#         print(num1, num2)
# except Exception as e:
#     print("Error is :", e)

# Problem no 2
# try:
#     user_input = input("Enter String : ")
#     if type(user_input) == str:
#         print("Your Input : ", user_input)
# except Exception as e:
#     print("Error is : ", e)

# Problem no 3
# try:
#     num1 = int(input("Enter number one : "))
#     num2 = int(input("Enter number two : "))
#     if type(num1 and type(num2) == int):
#         pass
# except:
#     print("Please enter valid input")
# finally:
#     print(f"The sum of {num1} and {num2} is : {(num1 + num2)}")

# Problem no 4
# try:
#     integer = int(input("Enter an integer: "))
#     print(integer)
# except ValueError:
#     print("The input is not an integer.")
# else:
#     print("The input is an integer.")

# Problem no 5
try:
    print(x)
except Exception as e:
    print(e)
except ValueError as v:
    print(v)
except:
    print("Some error occurred")
