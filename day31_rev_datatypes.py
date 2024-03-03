# 1. List
# List is muteable in python and Python list is ordered collection of data types
# my_list = ["Ayaz", 54, 32, 88, True, 81, "Khan"]
# # Length of List
# print("Length is : " , len(my_list))

# # Indexing
# print(my_list[len(my_list)-3])
# print(my_list[len(my_list)-1])

# # First index + last or desire index + jumping index
# print(my_list[0:7:3])

# # Now we are going to convert negative index to positive index
# print("Negative index : ", my_list[-5])
# print("Positive index : ", my_list[len(my_list)- 5])
 
# # Slicing of list
# my_list2 = ['p','r','o','g','r','a','m','i','z']
# print(my_list2[2:8]) #2 to 7
# print(my_list2[4:9]) #4 to 8

# # Methods of Python List
# #1. Append
# my_list3 = ["Apple", "Banana", "Orange"]
# print("List before : " , my_list3)
# my_list3.append("Mangoes")
# print("List after : ", my_list3)
# #2. extends
# even_numbers = [2,4,6,8]
# prime_numbers = [1,3,5,7]
# prime_numbers.extend(even_numbers)
# print(prime_numbers)
#3. insert
# new_list = [10,20,30,40]
# new_list.insert(2,"Ayaz khan")
# print("List : ", new_list)
#4. Remove
# languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
# languages.remove('R')
# print("New list : ", languages)
#5. Index
# languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
# ind = languages.index('R')
# print(ind)
#6. Pop
# languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
# res = languages.pop(1)
# print("Pop element : ", res)
# print("Updated List : ", languages)
#7. Count
# languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R', 'R']
# result = languages.count('R')
# print(result)
#8. sort
# prime_number = [1,3,5,7,11,13,19,17]
# prime_number.sort()
# print(prime_number)
# vowels = ['e', 'a', 'u', 'o', 'i']
# vowels.sort()
# print("Sorting vowels in asscending : ", vowels)
# vowels.sort(reverse=True)
# print("Sorting vowels in desending : ", vowels)
# _______________________________________________________________________________
#2. Tuples
# var1 = ("Hello world") #String
# var2 = ("Hello world",) #Tuple
# print(type(var1))
# print(type(var2))
#
# # Creating Tuple
# tup = (1,2,3)
# print(tup)
# print(type(tup))

# Indexing
# tup1 = ("Banana", "Orange", "Mango", "Apple")
# print(tup1[1])
# print("Length : ", len(tup1))
# print(tup1[len(tup1)-1])

# # Slicing
# tup2 = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
# print(tup2[len(tup2)-6])

# Tuple Methods

#1. Count
# my_tuple = ('a', 'p', 'p', 'l', 'e',)
# print(my_tuple.count('a'))
# print(my_tuple.count('e'))

#2. Index
# vowels = ('a', 'e', 'i', 'o', 'u',)
# print(type(vowels))
# result = vowels.index('u')
# print("INDEX : ", result)
# numbers = (2, 4, 6, 8, 10,)
# ind = numbers.index(6)
# print("Index : ", ind)
# _______________________________________________________________________________
#3. Sets
# Sets are immutable in Python
# set1 = {1, 2, 3, 4, 5, 6, 7, 2}
# print(set1)
# set2 = {"Ayaz Khan", "Khan", "Ayaz Khan", 2, 5}
# print(set2)
# print(len(set2))
# print(type(set2))

# Set methods
#1. Add
# prime_numbers = {1,3,5,7,9}
# prime_numbers.add(11)
# print("Updated List : ", prime_numbers)
#2. union
# prime_numbers = {1,3,5,7,9}
# even_numbers = {2,4,6,8}
# result = prime_numbers.union(even_numbers)
# print(prime_numbers)
# print(result)
#3. intersection
# num1 = {1,2,3,5}
# num2 = {2,3,5,10}
# result = num1.intersection(num2)
# print("Common elements : ", result)
#4. isdisjoint
# print(num1.isdisjoint(num2))
#5. Pop
# languages = {'a','y','a','z'}
# res = languages.pop()
# print("Pop element : ", res)
# print("Updated set : ", languages)
#6. Difference
# num1 = {1,3,5,7} # This set will print because difference meaning if the set A has all unique elements than set B A-B
# num2 = {2,4,6,8}
# print(num1.difference(num2))
#7. copy
# names = {'Ayaz','Khan', 'Irtaza', 'Ishtiaq'}
# result = names.copy()
# print("Orignal Names : ", names)
# print("Copy names : ", names)
# _______________________________________________________________________________
#4. Tuples
tup = {"Name": "Ayaz Khan", "Age": 15, "Rollnumber": "F20", "Name": "Ayaz"}
print(tup) # This will Print Ayaz becz it only print updated name, also dict is mutable , you can change the value of key but you cannt change the key
print(type(tup))
print(tup["Name"])# This will print ayaz

# Methods
#1. keys
print(tup.keys())
#2. values
print(tup.values())
#3. items
print(tup.items())
#4. pop
result = tup.pop("Name")
print("Pop element : ", result)
#5. get
print(tup.get("Age"))




