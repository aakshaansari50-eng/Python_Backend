# class Pattern:

#     def right_angle():
#         for i in range(1, 6):
#             print("*" * i)
            
#     def left_angel():
#         for i in range(1,6):
#             print(" "*(6-i),"*"*i)      
            
# p = Pattern

# p.right_angle()
# p.left_angel()

class pattern:
    def right_angel():
        for i in range(1,6):
            print("* "*i)            
p=pattern
p.right_angel()

class pattern1:
    def left_angel():
        for i in range(1,6):
            print(" "*(6-i),"*"*i)
            
p1=pattern1
p1.left_angel()

class pattern2:
    def triangel():
        for i in range(1,6):
            print(" "*(6-i),"* "*i)
            
p=pattern2
p.triangel()



class pattern3:
    def diamond():
        for i in range(1,6):
            for k in range(1,6-i):
                print(" ",end="")
            for j in range(1,i+1):
                print(" *",end="")
                
            print()
            
        for i in range(4,0,-1):
            for k in range(1,6-i):
                print(" ",end="")
            for j in range(1,i+1):
                print(" *",end="")
                            
            print()
            
p=pattern3
p.diamond()

class pattern4:
    def square():
        for i in range(5):
            print("* "*5)
            
        print("----------------------------")

p=pattern4
p.square()

class pattern5:
    def hourglass():
        for i in range(1,6):
            for k in range(1,6-i):
                print(" ",end="")
            for j in range(1,i+1):
                print("*",end=" ")
                        
            print()
                    
    for i in range(4,0,-1):
        for k in range(1,6-i):
            print(" ",end="")
        for j in range(1,i+1):
            print("*",end=" ")
                                    
        print()
            
p=pattern5
p.hourglass()       