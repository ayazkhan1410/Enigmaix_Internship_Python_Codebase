# File creating
# open("FileName", "Permission")
# course_outline = "This is revision File"
# file = open("Demo3.txt", "w")
# file.write(course_outline)
# print("File created successfully")
# file.close()

# Another example
# demo3 = "Again i am creating this file"
# file = open("Demo4.txt", "w")
# file.write(demo3)
# print("File created successfully")
# file.close()

# File read
# file = open("demo4.txt", "r")
# filecontent = file.read()
# print("Data : ", filecontent)

# Another example
# file = open("Demo3.txt", "r")
# file_content = file.read()
# print("Data : ", file_content)

# Storing a list into a file
# cities = ["Lahore", "Karachi", "Bahawalnagar"]
# file = open("Demo5.txt", "w")
# file.writelines(cities)
# print("File has been created ")
# file.close()

# Another example
# This will store in single String it only use single memory block
# fruits = ["Apple", "Mangoes", "Banana", "Orange"]
# file = open("Fruits.txt", "w")
# file.writelines(fruits)
# print("File has been created")
# file.close()

# Read a file from a list
# file = open("fruits.txt", "r")
# data = file.readline()
# print("Data : ", data)

# Another example
# file = open("Demo1.txt", "r")
# data = file.readline()
# print("Data : ", data)

# Problem No 1
# Creating a file
# str1 = "This is my last program on file"
# file = open("Demo6.txt","w")
# file.write(str1)
# print("File has been created")

# # Read a file
# file = open("Demo6.txt", "r")
# file_content = file.read()
# print("Data in File : ", file_content)

# Problem No 2
# file = open("Demo5.txt", "r")
# var = file.read()
# print("Content : ", var)

# Problem No 3
# input1 = input("Enter a text : ")
# file = open("Demo1.txt", "r")
# var1 = file.read()
# print(input1, var1)

# Problem No 4
# list1 = ["Apple", "Mango", "Orange"]
# file = open("Demo7.txt", "w")
# file.writelines(list1)
# print("File has been created")

# Problem No 5
# file = open("Demo7.txt","r")
# file_list = file.readlines()
# print("Content : ", file_list)