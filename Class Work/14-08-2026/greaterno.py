n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number: "))
n4=int(input("Enter the fourth number: "))
if n1>n2:
    if n1>n3:
        if n1>n4:
            print("The first number is greater.")
        else:
            print("The fourth number is greater.")
    else:
        if n3>n4:
            print("The third number is greater.")
        else:
            print("The fourth number is greater.")
else:
    if n2>n3:
        if n2>n4:
            print("The second number is greater.")
        else:
            print("The fourth number is greater.")
    else:
        if n3>n4:
            print("The third number is greater.")
        else:
            print("The fourth number is greater.")