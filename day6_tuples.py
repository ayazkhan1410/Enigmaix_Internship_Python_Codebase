 # Tuples are immuteable you can not change the value of the tuple
# # Different types of tuples
# # 1. Empty tuple
# tup = ()
# print(tup)
# #2. Tuple having an integers
# tup2 = (1,2,3,4,5)
# print("The type of tuple is : " , type(tup2))
# print("Integers tuples are : ",  tup2)
# #3. Different data types tuples
# tup3 = (1,"Green", True, [1,2,3,4],2.54)
# print("Different data types of tuples are : " , tup3)
# #4. Nested tuples are 
# tup4 = (2,"Yellow",[1,2,3],[3,2,1])
# print("Here is nested tuple : ", tup4)
# #5. Tuple without paranthese
# tup5 = 1,2,3,4,"Hello world", True, [1,2,3,4,5]
# print("Tuples without paranthese are : ", tup5)
# #6. Important thing
# var = (1) # this is called integer 
# print(type(var))
# tup6 = (1,) # This is called tuple using "," is important if you want 1 element tuple
# print(type(tup6))
#------------------------------
# Accessing element of the tuple
#1. INDEXING
#tup1 = ("Biryani", "Milk shake", True, 1,2,3,['Yello','Green','Red'])
# 0th index = Biryani, 1, Milk shake, 2 = True, 3 = 1, 4=2, 5=3, 6= Yellow, Green, Red
# print(tup1[2])
# print(tup1[6])
# #2. Negative indexing
# print("The length of tuple is  is : ", len(tup1))
# print(tup1[-1])
# print(tup1[-2])
# print(tup1[-6])
# print(tup1[-7])
#------------------------------
tup1 = ("Biryani", "Milk shake", True, 1,2,3,['Yello','Green','Red'])
#3. Slicing

# Positive Slicing
#print(tup1[0:7])
# Begining to the end
#print(tup1[:])
# just know the starting point
#print(tup1[1:])
# Just know the ending point'
#print(tup1[:7])

# Negative Slicing
print(tup1[-5:-1])