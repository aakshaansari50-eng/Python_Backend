class A:
    def fun1(self):
        print("Method 1!!")
        
class B(A):
    def fun2(self):
        print("Method 2!!")
        
class C:
    def fun3(self):
        print("Method 3!!")
        
class D(B,C):
    def fun4(self):
        print("Method 4!!")
        
obj=D()
obj.fun1()
obj.fun2()
obj.fun3()
obj.fun4()