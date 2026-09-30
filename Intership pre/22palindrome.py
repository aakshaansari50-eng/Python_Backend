def palindrome(no,rev=0,rem=0):
    n=no
    for i in range(no):
        if no==0:
            break
        
        rem=no%10
        rev=rev*10+rem
        no//=10
        
    if n==rev:
        print("Palindrome!!")
    else:
        print("Not Palindrome!!")
        
    return rev

no=int(input("Enter a Number : "))
palindrome(no)