class MyClass1:
    
    def fun1(self):
        print("Method 1!!")
        
class Myclass2(MyClass1):
    
    def fun2(self):
        print("Method 2!!")
        
obj=Myclass2()
obj.fun1()
obj.fun2()
        
    