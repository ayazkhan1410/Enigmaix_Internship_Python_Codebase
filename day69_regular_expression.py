# Match Function
import re

# 1. Match FUNCTION

# pattern = r"^ayaz khan"
# my_string = "ayaz khan"
# x = re.match(pattern,my_string)
# print(x)

# 2. Search Function

# text = "I am Batman"
# var1 = re.search("B",text)
# print("B is on : ",var1.start())

# 3. Replace Function

str1 = "This Course is free to earn"
print("Before Replace : ", str1)
x = re.sub(r"earn","Learn",str1)
print("After Replace : ", x)

str2 = "Hi MY Name is Patrick Bateman"
print("Before : ", str2)
y = re.sub(r"[a-z]","1",str2)
print("After : ", y)