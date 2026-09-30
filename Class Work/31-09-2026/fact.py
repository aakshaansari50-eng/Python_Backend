def fac(n):
    
    if n==1:
        return 1
    else:
        return n*fac(n-1)
    
        #5*fac(4)
        #4*fac(3)
        #3*fac(2)
        #2*fac(1)
        #1
    
n=int(input("Enter a Number : "))
print(fac(n))