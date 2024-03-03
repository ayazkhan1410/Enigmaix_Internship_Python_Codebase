


# Raising custom error in python
i = input("Enter number between 5 and 9")

if(int(i)<5 or int(i)>9):
    raise ValueError("Please enter  number between 5 and 9")
elif(i == 'quit'):
    print("GoOD GUESS")
else:
    print(i)