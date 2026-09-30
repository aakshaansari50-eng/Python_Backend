def prime_numer(n, prime=0):
    for i in range(1,n+1):
        if(n%i==0):
            prime+=1

    if(prime==2):
        print("Prime Number!!")
    else:
        print("Not a Prime Number!!")

n=int(input("Enter a Number :"))
prime_numer(n)

print("Reverse Number Code")

def rev_number(n,rem=0,rev=0):
    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n//=10
    print(rev)

n1=int(input("Enter a Number :"))
rev_number(n1)
