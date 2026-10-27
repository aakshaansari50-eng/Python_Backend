class User:
    def __init__(self,a,b):
        self.a=a
        self.b=b
          
    def __str__(self):
        return f"{self.a},{self.b}"
        
    def __add__(self,obj):
        x=self.a+obj.a
        y=self.b+obj.b
        return User(x,y)
    
    def __sub__(self,obj):
        x=self.a-obj.a
        y=self.b-obj.b
        return User(x,y)
    
    def __mul__(self,obj): 
        x=self.a*obj.a
        y=self.b*obj.b
        return User(x,y)
    
    def __truediv__(self,obj):
        x=self.a/obj.a
        y=self.b/obj.b
        return User(x,y)
            

obj=User(5,10)
print(obj)
obj1=User(10,20)
print(obj1)
print("Addition of two objects : ",obj+obj1)
print("Subtraction of two objects : ",obj-obj1)
print("Multiplication of two objects : ",obj*obj1) 
print("Division of two objects : ",obj/obj1)
        