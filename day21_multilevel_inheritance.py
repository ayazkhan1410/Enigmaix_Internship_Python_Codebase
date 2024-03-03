class GrandFather:
    def skincolor(self):
        print("Sking color is white")
    def eyecolor(self):
        print("Eye color is black")
    def height(self):
        print("Height is 5.6ft")
class Father(GrandFather):
    def strongbrain(self):
        print("Stong brain")
    def lifestylehabit(self):
        print("Luxury life style")
class Son(Father):
    def angerissue(self):
        print("I have anger issues")
# Creating objects
ss = Son()
ss.angerissue()
ss.eyecolor()
ss.height()
ss.lifestylehabit()
ss.skincolor()
ss.strongbrain()
                        