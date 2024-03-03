class StateBank: # This is our abstract class
    def intrest(self): # This is our abstract method
        pass # This is out abstract class syntax
    
class AlliedBank(StateBank):
    def intrest(self): # Calling Abstract methods
        print("Allied bank intrest is : 5%")
class HBL(StateBank): 
    def intrest(self): # Calling Abstract methods
        print("HBL intrest is : 7%")
class UBL(StateBank): # Calling Abstract methods
    def intrest(self):
        print("UBL bank intrest is : 8%")
class Meezan(StateBank):
    def intrest(self): # Calling Abstract methods
        print("Mezan bank intrest is 10%")
        
# Creating an object
aa = AlliedBank()
aa.intrest()
hh = HBL()
hh.intrest()
uu = UBL()
uu.intrest()
mm = Meezan()
mm.intrest()