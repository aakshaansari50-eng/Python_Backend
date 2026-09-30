def prime(n,i=2):
    if n==i:
        return 1
    if n%i==0:
        return 0
    else:
        return prime(n,i+1)
    
n=int(input("Enter a Number : "))
if prime(n):
    print("Prime!!")
else:
    print("Not a Prime!!")