def prime_no(no,prime=0):
    for i in range(1,no+1):
        if no%i==0:
            prime+=1
            
    if prime==2:
        print("Is Prime!!")
    else:
        print("Not a Prime!!")
            
    return prime
            
no=int(input("Enter a Number : "))
prime_no(no)
    