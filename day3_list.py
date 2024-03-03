ages = [12,15,17]
print(ages)
item_list = ["apple", "banana", "cherry", 2, 3, 4, 5]
print(item_list)
languages = ['python', "java", "c++", "c", "c#", "javascript", "php"]
print(languages[0])
print(languages[1])
print(languages[2])
print(languages[3])
print(languages[4])
print(languages[5])
print(languages[6])
# negative indexing
print("----- Negative indexing ------")
newlanguages = ["English", "French", "Spanish"]
print(newlanguages[-3])
print(newlanguages[-2])
print(newlanguages[-1])
# slicing of python list
my_list = ['p', 'R', 'o', 'G', 'r']
print(my_list[2:5])
## this will print list from 2 index to the end
print(my_list[2:])
## this will print list from Starting to end
print(my_list[:])
print("__________Python List methods______")
#Python List Methods
# Using append
print("__________ Append method ______")
age2 = [12, 15, 17]
print("Before append list : ", age2)
age2.append(20)
print("After append list : ", age2)
## Extend method
print("__________ Extend method ______")
prime_numbers = [2, 3, 5, 7]
even_numbers = [0, 2, 4, 6, 8]
print("Before extend list : ", prime_numbers)
prime_numbers.extend(even_numbers)
print("After using extend : ", prime_numbers)
#Change List items
mylist = ['A', 'B', 'C', 'D', 'E']
print("List before changing : ", mylist)
mylist[0] = 'Z'
print("List after changing : " , mylist)
del mylist[-1]
print("List after deleting : ", mylist)
print("New list ----------")
name6 = ['A','Y','A','Z']
del name6[-1]
print("List after deleting two indexs", name6)
print("remove method")
programming_languages = [ "Java", "Python", "Cpp", "C sharp"]
programming_languages.remove("Java")
print(programming_languages)
# pop method
prime_numbers2 = [2,3,5,7,11,13,17,19]
remove_ele = prime_numbers2.pop(2)
print("Removed element : ", remove_ele)
print("Updated list : " , prime_numbers2)
#reverse 
even_numbers3 = [0,2,4,6,8]
print("Before reverse : ", even_numbers3)
even_numbers3.reverse()
print("After reverse : ", even_numbers3)
#09 Copy list
mynumber = [1,2,3,4,5]
print("Before copy : ", mynumber)
newnumber = mynumber.copy()  # this will create shallow copy of list
print("After copy : ", newnumber)
#10 INDEX
mylist2 = ['A', 'B', 'C', 'D', 'E']
print("Index of A is : ", mylist2.index('A'))
print("Index of E is :  ", mylist2.index('E'))
#11 Count
mylist3 = ['A', 'B', 'C', 'D', 'E', 'A', 'A']
print("Count of A is :", mylist3.count('B'))
#12 insert
mylist4 = ["A","E","I","U"]
print("Before insert : ", mylist4)
mylist4.insert(3,"O")
print("After insert : ", mylist4)
# access String in python
# Indexing
greet = 'Hello'
'''#access first index element
print(greet[0])
#Negative indexing
print(greet[-4])
# slicing
print(greet[0:5])
# Strings are immuteable in python 
message = 'Hello Ayaz'
# we can assign new value to string
newmessage = 'Hello Ayaz Khan'
print(newmessage)
# negative slicing another look
name7 = 'hashmi'
print(name7[-6:-2])
'''
