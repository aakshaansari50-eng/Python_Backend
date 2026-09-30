def fibbo(no,a=0,b=1):
    for i in range(no):
        print(a,end=" ")
        
        c=a+b
        a=b
        b=c
    
    return a

no=int(input("Enter a Number :"))
print(fibbo(no))