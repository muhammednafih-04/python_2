import re
text=input("enter a text:")
'''print("1.search\n2.findall\n3.sub\n4.dot meta")
op=int(input("enter an option"))
if op==1:
    w=input("enter a word to search:")
    m=re.search(w,text)
    if m:
        print("matching found")
    else:
        print("no matches found")
elif op==2:
    f=input("enter word to search:")
    r=re.findall(f,text)
    print(r)
elif op==3:
    c=input("enter the character to change: ")
    s=input("enter a word to sub:")
    n=re.sub(c,s,text)
elif op==4:
    rs=findall(".at",text)
    print(rs)
else:
    print('invalid option')'''




res=re.findall("[cb]at",text)
print(res)
res=re.findall("[0-9]",text)
print(res)