age=int(input("Enter Age : "))
time=int(input("Enter Time : "))

if age >= 18:
    if time >= 22 or time <= 2:
        print("Order Allowed!!")
    else:
        print("Order not Allowed!!")
else:
    print("You are not eligible!!")