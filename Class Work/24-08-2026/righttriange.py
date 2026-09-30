"""for i in range(1,6): # right angel
    for j in range(1,i+1):
        print("*",end=" ")

    print()

for i in range(1,6): # one line right angel
   print("* "*i)
   """

for i in range(1,6): #left angel

    for k in range(1,6-i):
        print(" ",end=" ")

    for j in range(1,i+1):
        print("*",end=" ")

    print()


"""
for i in range(6,1): // Triangle
    print("*"*i)

for i in range(1,6):

    for k in range(1,6-i):
        print(" ",end="")

    for j in range(1,i+1):
        print(" *",end="")

    print()
"""
"""
for i in range(1,6): 

    for k in range(1,6-i):
        print(" ",end="")

    for j in range(1,i+1):
        print("*",end="")

    print()
  

for i in range(1,6): 
    print(" "*(6-i)," *"*i)
"""
for i in range(1,6): 
    print(" "*(6-i),"*"*i)
    