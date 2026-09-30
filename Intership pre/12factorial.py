no=int(input("Enter a Number : "))
fact=1

for i in range(1,no+1):
    fact=fact*i
    i+=1
    
print("Factorial is : ",fact)