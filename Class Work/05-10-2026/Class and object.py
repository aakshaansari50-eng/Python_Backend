class MyClass:
    
    def even_odd(self):
        no=int(input("Enter a Number : "))
        if no % 2 == 0:
            print("Even")
        else:
            print("Odd")
    
    def prime(self):
        no=int(input("Enter a Number : "))
        prime=0
        for i in range(1,no+1):
            if no % i == 0:
                prime+=1    
        if no==2:
            print("Prime")
        else:
            print("Not Prime")
        
    def factorial(self):
        no=int(input("Enter a Number : "))
        fact=1
        for i in range(1,no+1):
            fact=fact*i
            i+=1
        print("Factorial is : ",fact)

obj=MyClass()
obj.even_odd()
obj.prime()    
obj.factorial()