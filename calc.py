class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
c=calculator()
a=int(input("enter first number:"))
b=int(input("enter second number:"))
print("addition=",c.add(a,b))
print("subtraction=",c.sub(a,b))
print("multiplication=",c.mul(a,b))
print("Division=",c.div(a,b))

