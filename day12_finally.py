# try:
#  list1 = [1,3,5,6]
#  i = int(input("Enter an index"))
#  print(list1[i])
# except:
#     print("Some error occured")
# finally:
#     print("I will always excute")

def successfully():
    try:
        lst = []
        ele = int(input("Enter number of element you want to insert in a list : "))
        for i in range(0,ele+1):
         element = int(input(f"Enter {i} index element"))
         lst.append(element)
         print(lst)
    except :
        print("INVALID input from the user")
    finally:
        print("-----------------")
        print("The program has been successfully executed")
        print("End of the program")
        
x = successfully()
print(x)