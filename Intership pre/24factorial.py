def factorial(no,fact=1):
    for i in range(1,no+1):
        fact=fact*i
        i+=1
        
    return fact

no=int(input("Enter a Number : "))
print(factorial(no))