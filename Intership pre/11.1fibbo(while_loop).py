no=int(input("Enter a Number : "))
a=0
b=1
i=1

while i<=no:
    print(a,end=" ")
    
    c=a+b #0+1=1
    a=b  #1
    b=c #1

    i+=1