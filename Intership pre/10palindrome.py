no=int(input("Enter a Number :"))
rem=0
rev=0
n=no

for i in range(no):
    if no==0:
        break
    
    rem=no%10
    rev=rev*10+rem
    no//=10
    
print("Reverse is :",rev)

if n==rev:
    print("Palindrome!!")
else:
    print("Not palindrome!!")