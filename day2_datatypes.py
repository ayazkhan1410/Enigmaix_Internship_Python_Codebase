## String operations in python

## 1. Compare operator
str1 = "Hello world"
str2 = "I love python"
str3 = "Hello world"
## now we compare str1 with str2
print(str1==str2)
## next we will compare str1 with str3
print(str1==str3) ## This will return answer true because both Strings are equl to each other
## now again we will compare str2 with str3
print(str2==str3)
## in compare operator we get result in case of true and false

# 2. join TWO OR MORE Strings in python
fname = "Ayaz"
lname = "Khan"
result = fname + lname ## we use + operator to join two or more string in python
print(result)

# 3. Iterate
greet = 'Hello world'
for letter in greet:
    print(letter)
# 4. String length
greet2 = 'ayaz khan'
print("The is a length of greet : ", len(greet))
print("This is a length of greet2 : ",  len(greet2))
# 5. Membership 
name3 = 'Ayaz'
print('a' in 'name3')
print('n' not in 'name')
#6. upper
messgae = 'i love python'
print(messgae.upper())
# example
stri = 'Hi my name is ayaz khan'
stri2 = ' Hi my name is'
if(stri.upper() == str2.upper()):
 print('the strings are same')
else: 
 print('The strings are not same')
# 7. Lower
messgae2 = 'I LOVE JAVA'
print(messgae2.lower())
if(messgae2.lower() == greet2.lower()):
   print("The String are so far not same")
else: 
   print("The program has been terminated without any error")
   # 8. Swapcase
   name4 = 'Ayaz KHAN'
   print(name4.swapcase())
   name5 = ' this MIGHT be MIXED'
   print(name5.swapcase())
   #9 . capitalize
   mor = 'please do like and subscribe'
   print(mor.capitalize())
   #10 center 
   txt = 'python is love'
   print(txt.center(70))
   #11 count
   txt2 = "I love apple, and everyone should love apples"
   print(txt2.count('apple'))
   #12 title 
   txt3 = "i love to watch youtube videos"
   print(txt3.title())
   #13 Index
   txt4 = 'Hi guys whatsup'
   print(txt4.index('guys'))
   #14 Find
   txt5 = 'Python is fun programming language'
   print(txt5.find('is'))
   #15 replace 
   text6 = 'Bat ball'
   print(text6.replace('Ba', 'lu'))
   print(text6.replace('ba', 'cu'))
   #16 endswith
   txt7 = 'please do like and subscribe'
   print(txt7.endswith('subscribe'))
   #example
   if(txt7.endswith('subscribe')):
    print("Huraah you win the game")
   else:
      print("You lost the game badly")
      
'''#Integers
print("------------ Integers -------------")
print(num1, ' is a type of ', type(num1))
print(num2, ' is a type of ', type(num2))
print(num3, ' is a tpe of ',  type(num3))
print(num4, ' is a type of ', type(num4))
print("------------ Complex numbers -------")
print(num5, ' is a type of ', type(num5))
print(num6, ' is a type of ' , type(num6))
print("------------- Float --------------")
print(num7, ' is a type of ', type(num7))
print(num8, ' is a type of ', type(num8))
'''

'''
#Create a String using double quotes
string1 = "Hi i am double quotes String"
string2 = 'Hi i am single quotes String'
print(string1)
print(string2,type(string2))
# Create String using variable
name = "java"
print(name)
name2 = "I love java"
print(name2)
## multiline string
message = """"
hi i am a multiline String
i can write code in multi line
"""
print(message)
'''


