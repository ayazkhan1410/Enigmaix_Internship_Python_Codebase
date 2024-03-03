from functools import reduce
# Map
def square(n):
    return n*n
ss = square(5)
print(ss)
lst = [1,2,3,4,5]
newl = list(map(square,lst))
print(f"Square list : {newl}")

def cube(x):
    return x*x*x
c = cube(3)
print(c)

l = [2,4,5,6,8,10]
newll = list(map(cube,l))
print("Cube list: " , newll)

#Filter
def filter_function(num):
    return num<4 # This will filtered and give only number whch are less than 4
newnewl = list(filter(filter_function,l))
print("Filtered : ", newnewl)

newlll = list(filter(filter_function,lst))
print("2nd filtered : ", newlll)

# Reduce
number1 = [1,2,3] # this is list 
def mysum(num1, num2): # now we create mysum function
    return (num1+num2) * 2 # after that we are returining this
result = reduce(mysum,number1) # now reduce function what it will do is it simply take first 1+2 and multipliy this answer with 2 means 1+2=3*2=6 next again 6+3=9*2=18
print("Result : ", result)