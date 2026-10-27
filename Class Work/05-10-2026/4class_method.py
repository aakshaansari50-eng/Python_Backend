class MyClass1:
    
    def even_odd(self, no):
        if no % 2 == 0:
            print(no , "Is Even")
        else:
            print(no , "Is Odd")
            
class MyClass2:
    
    def prime(self,no,prime=0):
        for i in range(1,no+1):
            if no % i == 0:
                prime+=1    
        if prime==2:
            print(no ,"Is Prime")
        else:
            print(no ,"Is Not Prime")
        
class MyClass3:
    
    def factorial(self, no):
        fact=1
        for i in range(1,no+1):
            fact=fact*i
            i+=1
        print("Factorial is : ",fact)
        
class MyClass4:
    
    def fibbo(self,no,a=0,b=1):
        for i in range(no):
            print(a,end=" ")
            c=a+b
            a=b
            b=c

obj1=MyClass1()
obj2=MyClass2()
obj3=MyClass3()
obj4=MyClass4()

no=int(input("Enter a Number : "))
obj1.even_odd(no)
obj2.prime(no)    
obj3.factorial(no)
obj4.fibbo(no)
        