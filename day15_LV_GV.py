x = 4 # This is global variavble
print(x)
def sum():
    global y # This keyword is used to create x as a global variable
    y = 10
    num1 = 5 # This is local variable we can only access this within a class
    num2 = 10 # This is local variable we can only access this within a class
    print("Sum : ", num1+num2) 

# print(num1) #This will generate an error bcz we cannot access this here
# print(num2) # Throwing an ---> error
print(f"Global Variable : " , x)
sum()
print(f"Global keyword : {y}")