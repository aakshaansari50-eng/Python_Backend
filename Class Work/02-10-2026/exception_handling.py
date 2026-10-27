# try:
#     n=int(input("Enter a Number : "))
    
#     if n==0:
#         print("Number is Zero")
#     else:
#         print("Number is not Zero")
        
# except ValueError as e:
#     print(e)
    
# else:
#     print("Try Here!!")
    
# finally:
#     print("Everytime!!")

#1) ValueError
#2) ZeroDivisionError

# try:
#     n=int(input("Enter a Number 1 : "))
#     n1=int(input("Enter a Number 2 : "))
    
#     print("Division is : ",n/n1)

# except ValueError as e:
#     print(e)

# except ZeroDivisionError as e:
#     print(e)

# Index Error     
# try:       
#     l=[78,45,36,21,15,12,10]
    
#     n=int(input("Enter Index :"))
#     print("Value Of Index is : ",l[n])

# except ValueError as e:
#     print(e)

# except IndexError as e:
#     print(e)

# handle all errors
try:
    l=[78,45,36,21,15,12,10]
    n=int(input("Enter Index :"))
    print("Value Of Index is : ",l[n])
    
except Exception as e:
    print(e)
    print("Invalid Input!!")
    

    