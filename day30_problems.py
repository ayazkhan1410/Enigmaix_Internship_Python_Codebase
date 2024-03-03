# Problem no1
# def panagram(scentence):
#     a = set(scentence.lower())
#     if(len(a) == 26):
#         print("True")
#     else:
#         print("False")
# s = "Ayaz Khan"
# s1 = "abcdefghijklmnopqrstuvwxyz"
# panagram(s)
# panagram(s1)

# Problem no 2
# user_input = int(input("Enter the number : "))
# if(user_input<0):
#     a = abs(user_input)
#     print(a)
# else:
#     print(user_input)

# Problem no 3
# def longest(s1, s2):
#     combined = s1+s2 #Combine strings
#     remove_duplicate = ''.join(set(combined)) #Remove duplicate
#     sorted_char= sorted(remove_duplicate)
#     return ''.join(sorted_char) 
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# result = longest(a, b)
# print(result)

# Problem no 4
# def opposite(number):
#    return -number
# print(opposite(1))
# print(opposite(14))
# print(opposite(-34))

# Problem no 5
# import math
# def calculatewater(hours):
#     water_intake = hours *0.5
#     div = math.floor(water_intake)
#     return div
# hours = 11.8
# cc = calculatewater(hours)
# print("Natan will drink : ", cc , " Liters of water") 

# Problem no 6
# def sort_odd_numbers(array):
#     odd_numbers = sorted([num for num in array if num % 2 != 0])
#     sorted_array = []
#     odd_index = 0

#     for num in array:
#         if num % 2 != 0:
#             sorted_array.append(odd_numbers[odd_index])
#             odd_index += 1
#         else:
#             sorted_array.append(num)

#     return sorted_array
# array1 = [7, 1]
# print(sort_odd_numbers(array1))  # Output: [1, 7]

# array2 = [5, 8, 6, 3, 4]
# print(sort_odd_numbers(array2))  # Output: [3, 8, 6, 5, 4]

# array3 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# print(sort_odd_numbers(array3))  # Output: [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

# Problem no 7
# def sumofnumbers(s1, s2):
#     if(s1 == s2):
#         print(1)
#     else:
#         print(s1+s2)
# user_input = int(input("Enter number one : "))
# user_input2 = int(input("Enter number two : "))
# sumofnumbers(user_input,user_input2)

# Problem no 8
# def findNeddle(lis1):
#     for item in lis1:
#         if(item == "needle"):
#             print("ITEM FOUND")
#         else:
#             continue
# lis1 = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
# findNeddle(lis1)

# Problem no 9
# def summation1(num):
#     sum = 0
#     for i in range(1, num +1):
#         sum += i
#     return sum
# user_input = int(input("Enter number : "))
# result = summation1(user_input)
# print("The summation is : " , result )

# Problem no 10
# def triangle(num):
#     return num **3
# print(triangle(4))

# Problem 11
# Pending

# Problem 12
# def petrochecker(fuelleft, nearestpetrolpump):
#     average = 25
#     dis = fuelleft * average 
#     return dis>= nearestpetrolpump
# fuelleft = int(input("Enter the gallon fuel left : "))
# nearestpetrolpump = int(input("Enter the distance of nearest petrol pumpt : "))
# aa = petrochecker(fuelleft, nearestpetrolpump)
# print(aa)

# Problem no 13
text = "How can mirrors be real if our eyes aren't real"
result = text.title()
print(result)