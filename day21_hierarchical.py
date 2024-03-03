class Father:
    name = "Ishtiaq Khan"
    def show(self):
        print(f"{self.name}")
class Ayaz(Father):
    name2 = "Ayaz khan"
    def show2(self):
        print(f"My name is {self.name2} and my father name is {self.name}")
class Sidrah(Father):
    name3 = "Sidra"
    def show3(self):
        print(f"My name is {self.name3} and my father name is {self.name}")
        
# Creating objeet
print("*** Father class ****")
ff = Father()
ff.show()
print("*** Son class ****")
ss = Ayaz()
ss.show2()
print("*** Daughter class ****")
dd = Sidrah()
dd.show3()