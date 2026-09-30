l=[]
ev=[]
od=[]
n=int(input("Enter a Number : "))
for i in range(1,n+1):
    l.append(i)
    if i%2==0:
        ev.append(i)
    else:
        od.append(i)
print("Even Numbers : ",ev)
print("Odd Numbers :",od)
     