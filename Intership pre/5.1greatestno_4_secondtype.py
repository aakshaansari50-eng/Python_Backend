no1=int(input("Enter a Number 1 : "))
no2=int(input("Enter a Number 2 : "))
no3=int(input("Enter a Number 3 : "))
no4=int(input("Enter a Number 4 : "))

if no1>no2:
    if no1>no3:
        if no1>no4:
            print("Number 1 is Greater!!")
        else:
            print("Number 4 is Greater!!")
    else:
        if no3>no4:
            print("Number 3 is Greater!!")
        else:
            print("Number 4 is Greater!!")   
else:
    if no2>no3:
        if no2>no4:
            print("Number 2 is Greater!!")
        else:
            print("Number 4 is Greater!!")
    else:
        if no3>no4:
            print("Number 3 is Greater!!")
        else:
            print("Number 4 is Greater!!")
