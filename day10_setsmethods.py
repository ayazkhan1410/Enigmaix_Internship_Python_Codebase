# Sets methods
# 1. Union 
# set1 = {"Pakistan", "Bangladesh", "India"}
# set2 = {"England", "Newzeland", "Australia"}
# a = set1.union(set2)
# #print(a)

# # 02. Update union
# b = set1.update(set2)
# print(set1) # this will update set1 and also print all elements 0f set2 in set1

#03. Intersection
# set1 = {"Pakistan", "Bangladesh", "India"}
# set2 = {"England", "Newzeland", "Australia","Pakistan"}
# result = set1.intersection(set2)
# print(result)

#04. Intersection update
# set1 = {"Pakistan", "Bangladesh", "India"}
# set2 = {"England", "Newzeland", "Australia", "Pakistan", "Bangladesh"}
# set1.intersection_update(set2)
# print(set1)

#05. Symmetric
# This will print those elements who are not common
# set1 = {"Pakistan", "Bangladesh", "India"}
# set2 = {"England", "Newzeland", "Australia"}
# res = set1.symmetric_difference(set2)
# print(res)

#06. Difference
# This will print element which are only in set1 but not in set2
# set1 = {"Pakistan", "Bangladesh", "India"} 
# set2 = {"England", "Newzeland", "Australia", "Pakistan"}
# res = set1.difference(set2)
# print(res)

#07. Isdisjoint
# set1 = {"Pakistan", "Bangladesh", "India"}
# set2 = {"England", "Newzeland", "Australia"}
# res = set1.isdisjoint(set2)
# print(res)

#08. Issuperset
# set1 = {"Pakistan", "Bangladesh", "India"}
# set2 = {"India","Pakistan"}
# print(set1.issuperset(set2))

#09 issubset
# setA = {1,2,3}
# setB = {1,2,3,4,5}
# print(setA.issubset(setB))

#10. add
# set1 = {"Pakistan", "Bangladesh", "India"}
# set2 = {"England", "Newzeland", "Australia"}
# set1.add("Srilanka")
# print(set1)

#11. Remove/discard
# set1 = {"Pakistan", "Bangladesh", "India"}
# set2 = {"England", "Newzeland", "Australia"}
# set1.remove("Aus") # This line will through an error
# set1.discard("England") # And this line will not through any kind of error

#12. Pop
# set1 = {"Pakistan", "Bangladesh", "India"}
# set2 = {"England", "Newzeland", "Australia"}
# temp = set1.pop()
# print("New set : ", set1)
# print("Pop item : ", temp)

# #13. Del
# del set2

#14. Clear
# set1 = {"Pakistan", "Bangladesh", "India"}
# set2 = {"England", "Newzeland", "Australia"}
# cc = set1.clear()
# print("New set : ", cc)