class A:
    _a = 10
    __b = 20
    def show(self):
        print("protected variable : ", self._a)
        print("Private variable : ", self.__b)
class B(A):
    def show(self):
        print("Accessing protected variable : ", self._a)
        # print("Accessing private variable : ", self.__b) # you cannot access this
bb = B()
bb.show()