no=int(input("Enter a Number : "))
prime=0

for i in range(1,no+1):
    if no%i==0:
        prime+=1
        
if prime==2:
    print("Prime!!")
else:
    print("Not Prime!!")