# class Override:
#     def fun1(self):
#         print("Method 1!!")
        
# class Override1(Override):
#     def fun1(self):
#         super().fun1()
#         print("Method 2!!")
        
# obj=Override1()
# obj.fun1()

class A:
    def fun1(self):
        print("Method 1!!")
        
class B:
    def fun1(self):
        super().fun1()
        print("Method 2!!")
        
class C(B,A):
    def fun1(self):
        super().fun1()
        print("Method 3!!")
        
obj=C()
obj.fun1()