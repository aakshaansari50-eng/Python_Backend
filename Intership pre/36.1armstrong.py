def arm(no,sum=0):
    temp=no
    
    while no>0:
        digit=no%10
        sum=sum+digit**3
        no//=10
    
    if sum==temp:
        print("Armstrong!!")
    else:
        print("Not a Arnstrong!!")
        
    return sum
        
    
no=int(input("Enter a Number : "))
arm(no)