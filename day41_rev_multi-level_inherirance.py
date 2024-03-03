class GrandFather:
    color = " "
    name = "Umer Daraz"
    def skincolor(self):
        print("Black")
        print("GrandFather name : ", self.name)
class Father(GrandFather):
    fathername = "Ishtiaq"
    def eyecolor(self):
        print("Eye color is Black")
        print("Father name : ", self.fathername, " " + self.name)
class Son(Father):
    son_name = "Ayaz"
    def height(self):
        print("Height is : 5.6 ft")
        print("Son name : ", self.son_name, " " + self.fathername)
ss = Son()
ss.color = "White"
print(ss.color)
ss.skincolor()
ss.eyecolor()
ss.height()