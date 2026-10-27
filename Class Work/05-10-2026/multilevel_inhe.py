class MyClass1:
    
    def fun1(self):
        print("Method 1!!")
    
class MyClass2(MyClass1):
    
    def fun2(self):
        print("Method 2!!")
        
class MyClass3(MyClass2):
    
    def fun3(self):
        print("Method 3!!")
        
obj=MyClass3()
obj.fun1()
obj.fun2()
obj.fun3()