# 1st parent class
class Ayaz:
    back = "Oracle and Java "
    def backend(self):
        print(f"implementing Backend development using : {self.back}")
# 2nd Parent 
class Abbas:
    front = "Html, CSS, Javascript"
    def frontend(self):
        print(f"Implementing Frontend development using : {self.front}")
# Creating Child class
class TeamLead(Ayaz, Abbas):
    def dynamic(self):
        print("Dynamic website created")
# Creating object
tt = TeamLead()
tt.backend()
tt.frontend()
tt.dynamic()