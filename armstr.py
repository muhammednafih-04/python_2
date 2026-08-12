num=int(input("enter a numbrer:"))
a=num
sum=0
total=len(str(a))
while num>0:
    digit=num%10
    num=num//10
    sum+=digit**total
if sum==a:
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")