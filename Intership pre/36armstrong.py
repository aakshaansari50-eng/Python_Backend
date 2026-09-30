no=int(input("Enter a Number : "))

temp=no
sum=0

while no>0:
    digit=no%10
    sum=sum+digit**3
    no//=10
    
if sum==temp:
    print("Armstrong!!")
else:
    print("Not a Armstrong!!")