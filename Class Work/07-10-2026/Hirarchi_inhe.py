class A:
    def fun1(self):
        print("Method 1!!")
        
class B(A):
    def fun2(self):
        print("Method 2!!")
        
class C(A):
    def fun3(self):
        print("Method 3!!")
        
obj=C()
ob=B()
ob.fun1()
ob.fun2()
obj.fun3()