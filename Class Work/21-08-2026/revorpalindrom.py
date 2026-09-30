n=int(input("Enter Number :"))
rev=0
rem=0
n1=n

while(n!=0):
    rem=n%10 #5836%10=583.6 58.3
    rev=rev*10+rem #0+6=6 60+3=3
    n//=10 #583 58

print(rev)

"""if n1==rev:
    print("Palindrome!!")
else:
    print("NOt Palindrome!!")
    """