# Parent class of B and C
class A:
    def method1(self):
        print("This is A class method")
# Parent class of D
class B(A):
    def method2(self):
        print("This is B class method")
class C(A):
    def method3(self):
        print("This is C class Method")
# Child class of B and C
class D(B,C):
    print("This is class D method")
C = C()
C.method1()
C.method3()
D = D()
D.method2()
D.method1()