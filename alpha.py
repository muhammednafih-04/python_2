v=0
c=0
up=0
low=0
f=open("sp.txt","r")
l=f.read()
for i in l:
    if i.isalpha():
        if i in "AEIOUaeiou":
            v+=1
        else:
            c+=1
        if i.isupper():
            up+=1
        if i.islower():
            low+=1
print("the no:of vowels:",v)
print("the no:of consonents:",c)
print("the no:of uppercase characters:",up)
print("the no:of lowercase charcters:",low)
f.close()
