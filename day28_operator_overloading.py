class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    def __add__(self, x):
        return f"{self.i + x.i}i - {self.j + x.j}j -  {self.k + x.k}k"
    def __sub__(self, x):
        return f"{self.i - x.i}i - {self.j - x.j}j - {self.k - x.k}k"
# Printing values
v1 = Vector(1,2,3)
print(v1)
v2 = Vector(4,5,6)
print(v2)
print(v1+v2)
print("-----------------")
#using minus method
v3 = Vector(10,8,6)
print(v3)
v4 = Vector(5,3,1)
print(v4)
print(v3-v4)