# First lets calculate the factorial of a number
def fact(n):
    '''
    This program take the input from the user and then display the factorial
    '''
    if(n == 0 or n==1):
        return 1
    else:
        return n * fact(n-1) # 5 * 4 * 3 * 2

num = int(input("Enter the number to take factorial : ")) #num =5
a = fact(num)
print("The factorial is : ", a)
print(fact.__doc__)

# Fabonaci series

def fab(num):
    if num == 0 or num == 1 or num == 2:
        return 1
    else:
        return fab(num-1) + fab(num-2)
a = fab(5)
print(a)
