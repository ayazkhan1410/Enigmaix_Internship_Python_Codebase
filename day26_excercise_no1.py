# PROBLEM 01
# assigning value
a = 10
# reassigning value
a = 12 # This will excecute because python variables are immuteable
# Printing value
print(a)

# Problem 02
# list1 = [1,2,3,4]
# list1.append(5)
# print(list1)

# Problem no 03
# def fun(n, s): 
#     return s*n
# number = int(input("Enter the number of time you want to print letter : "))
# scentence = input("Enter the scentence : ")
# aa = fun(number, scentence)
# print(aa)

# Problem 04
n = '35231'
print(list(n))
res = reversed(n)
print(list(res))

def reverse_digit(number):
    digit = []
    while number > 0:
        digit.append(number)
        digit.reverse()
    return digit
number = [1,2,3,4,5]
res = reverse_digit(number)
print(res)
# Problem 05
def initials(name):
    # Split the name into two words
    words = name.split(' ')
    # Get the first letter of each word and put them together
    initials = words[0][0] + '.' + words[1][0]
    # Return the initials
    return initials
print(initials("Ayaz Khan"))

# Problem 06
def func1(name):
    words = name[1:len(name)-1]
    return words
name1 = input("Enter any number to remove firs and last index : ")
f = func1(name1)
print(f)

# Problem 07
def check_duplicate(arr, input):
    input = int(input("Enter the number to check : "))
    if input in arr:
        print("Member in list")
    else:
        print("Not")
arr = [1,2,3,4,5,6,7,8]
check_duplicate(arr,input)

# Problem 08
def converter(user_input):
    temp1 = str(user_input)
    return temp1
user_input = int(input("Enter a number to convert into a String : "))
rr = converter(user_input)
print(f"Your String is '{rr}' ")

# Problem 09
def ends_with(string, substring):
  """Returns True if the first argument(string) passed in ends with the 2nd argument (also a string)."""
  if len(substring) > len(string):
    return False
  return string[-len(substring) :] == substring

print(ends_with("Ayaz KHAN", "KHAN"))
print(ends_with("Ishiaq", "hello"))

