def rev_no(no,rev=0,rem=0):
    for i in range(no):
        if no==0:
            break
        
        rem=no%10
        rev=rev*10+rem
        no//=10
        
    return rev

no=int(input("Enter a Number : "))
print(rev_no(no))