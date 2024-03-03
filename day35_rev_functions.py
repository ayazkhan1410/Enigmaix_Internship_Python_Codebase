#1. Creating Function
# def greet():
#     print("Good morning")
# greet()

#2. function with arguments
# def sum(a,b):
#     return a+b
# res = sum(5,6)
# print(f" The sum of {5} and {6} is : {res}")

#3.  Built-in Function
# print("Hello")
# x = round(54.3453,2) # This will return first two numbers after 54
# print(x)
# for i in range(1,11):
#     print(i)

#4. user-defined function
# def states(state='Punjab'):
#     print("State is : ", state)
# states()
# states('KPK')
# states('Sindh')
# states('Balochistan')

#5. Passing a list into function
# def my_func(fruits):
#     for item in fruits:
#         print(item)
# f = ["Apple", "Mangoes", "Orange", "Banana"]
# my_func(f)

#6. Recursion functions
# def fact(num):
#     if num == 1:
#         return 1
#     else:
#         return num * fact(num-1)
# user_input =int(input("Enter the number : "))
# res = fact(user_input)
# print(f"The factorial of {user_input} is {res}")
# This is how we can achieve recursion in Python

#7. lambda function
# x = lambda a,b : a*b
# print(f"The multiplcation of {5} and {7} is : {x(5,7)}")
# y = lambda a,b: a/b
# print(y(10,5))
# z = lambda a,b : a+b
# print(z(12,43)
# k = lambda a,b : a-b
# print(k(10,5))

#8. Global variable
# z = 25
# def my_func():
#     global z # through this we make z as a global variable
#     print(z) # 25
#     z = 20 # Updating value of z
#     print("Updated z : ", z) #20
# my_func() # Printing function

#9. local variable
# def multiplication(x,y):
#     multi = x*y # this x,y is local variable we can't access them from our main method
#     return multi
# result = multiplication(5,6)
# print(f"The multiplcation of {5} and {6} is {result}")
# not possible
# print(x)
# print(y)