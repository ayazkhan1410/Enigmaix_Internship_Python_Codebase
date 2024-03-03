# strongteams = {1: "PAKISTAN" , 2: "INDIA", 3: "ENGLAND", 4: "SouthAfrica"}
# print(strongteams) # This will print the whole dict with keys
# for key in strongteams: # THIS WILL PRINT THE KEYS OF THE STRONG TEAMS
#     print(key)

# # Add element to a python dic
# items = {1: "Apple", 2: "Mango", 3: "Orange"}
# print("Items : ", items)
# items ["4"] = "Banana" # This will only add key index wla scene nhn hy ism
# print("Updated Items : ", items)

# Update a value 
# capital_cities = {'Pakistan' : "Islamabad", 'India': "Delhi", 'Japan':"Tokyo", 'Turkey':"Istanbol"}
# print("without updated :" , capital_cities)
# capital_cities['Banglades'] = "Dhaka"
# print("Updated capital cities : ", capital_cities)

#Change a value in dict
# capital_cities = {'Pakistan' : "Islamabad", 'India': "Delhi", 'Japan':"Tokyo", 'Turkey':"Istanbol"}
# capital_cities['Pakistan'] = "Bahwalnagar"
# print("Updated Capital cities : ", capital_cities)

# Removing element
# capital_cities = {'Pakistan' : "Islamabad", 'India': "Delhi", 'Japan':"Tokyo", 'Turkey':"Istanbol"}
# del capital_cities['Pakistan']
# print("Updated dict : ", capital_cities)

# Get Key
# capital_cities = {'Pakistan' : "Islamabad", 'India': "Delhi", 'Japan':"Tokyo", 'Turkey':"Istanbol"}
# temp = capital_cities.keys()
# print("Keys are : ", temp)


items = {'Fruits' : "Banana" , 'Shakes' : "Milkshakes", 'Food' : "Karahi"}
print(items.items())  
for key, Value in items.items():
    print(f"The value corresponding to the key is {key}, is {Value}")
