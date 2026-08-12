class student:
    def name(self):
        self.a=input("entr a name:")
        self.r=int(input("enter roll no:"))
class sports(student):
    def addsports(self):
        self.s=input("enter sport name")
    def show(self):
        print("\nname=",self.a)
        print("rollno:",self.r)
        print("sports:",self.s)
obj=sports()
obj.name()
obj.addsports()
obj.show()

