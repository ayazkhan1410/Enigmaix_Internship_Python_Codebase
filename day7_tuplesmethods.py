#1. Concatination
# strongteams = ("Pakistan", "India", "Newzeland")
# lousyteams = ("Westindies", "Bangladesh")
# groupA = strongteams + lousyteams
# print(groupA)
# # Count
# tup1 = (1,2,3,4,5,6,8,1,2,4,5,2,1)
# res = tup1.count(1)
# print("Count of 1 is : ", res)

#3. Indexing
# tup1 = (1,2,3,4,5,6,8,1,2,4,5,2,1)
# res = tup1.index(2, 3, 10)
# print(res)

#4. Converting tuple into List to use the methods of list

strongteams = ("Pakistan", "India", "Newzeland")
temp = list(strongteams)
temp.append("Bangladesh")
temp.append("Westindies")
temp.insert(0,'Afg')
#print("This is list : ", temp) 
strongteams = tuple(temp)
print("This is tuple : ", strongteams)