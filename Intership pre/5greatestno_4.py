no1=int(input("Enter Number 1 : "))
no2=int(input("Enter Number 2 : "))
no3=int(input("Enter Number 3 : "))
no4=int(input("Enter Number 4 : "))

if no1>no2 and no1>no3 and no1>no4:
    print("1st Number is Greater!!")
elif no2>no3 and no2>no4 and no2>no1:
    print("2nd Number is Greater!!")
elif no3>no4 and no3>no1 and no3>no2:
    print("3rd Number is Greater!!")
else:
    print("Fourth Number is Greater!!")