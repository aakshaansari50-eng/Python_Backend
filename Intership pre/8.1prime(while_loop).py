no=int(input("Enter a Number :"))
prime=0
i=1

while i<=no:
    if no%i==0:
        prime+=1
    i+=1
    
if no==2:
    print("Is Prime!!")
else:
    print("Not Prime!!")