#1. File creating
name = "Hello My name is Ayaz khan"
file = open("Demo1.txt", "w")
file.write(name)
print("File has been created")
print("-------------")
file.close()

#2. File Read
file = open("Demo1.txt", "r")
filecontent = file.read()
print(filecontent)
file.close()

#3. Storing list into a file
lst = ["Java\n" , "Python\n" , "Php\n"]
file = open("Demo2.txt","w")
file.writelines(lst) # we use writelines method in python to store a list and it take list as a single String
print("File has been Created")
file.close()

#4. Read a list from a File
file = open("Demo2.txt","r")
filelistcontent = file.readlines() # WE use Readlines method to read a list from a fILE
print(filelistcontent)
file.close() 

#5. Appending the value into a file
city = " I am from Bahawalnagar"
file = open("Demo1.txt","a")
file.write(city)
print("File has been update")
file.close()

#6. Appending demo2.txt
languages = "Cpp"
file = open("Demo2.txt","a")
file.write(languages)
print("File updated")
file.close()

