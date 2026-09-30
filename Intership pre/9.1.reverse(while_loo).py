no=int(input("Enter a Number : "))
rev=0
rem=0

while no!=0:
    rem=no%10
    rev=rev*10+rem
    no//=10

print("Reverse Number is : ",rev)