class A:
    def fun1(self):
        print("Method 1!!")
        
class B:
    def fun2(self):
        print("Method 2!!")
        
class C(A,B):
    def fun3(self):
        print("Method 3!!")
        
obj=C()
obj.fun1()
obj.fun2()
obj.fun3()