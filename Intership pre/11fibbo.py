no=int(input("Enter Number : "))
a=0
b=1

for i in range(no):
    print(a,end=" ")
    
    c=a+b
    a=b
    b=c
