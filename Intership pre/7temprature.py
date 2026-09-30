temp=float(input("Enter a Temprature :"))

if temp>=50:
    print("Invalid Temprature!!")
elif temp>=40 and temp<=50:
    print("Very Hot!!")
elif temp>=30 and temp<=40:
    print("Normally Hot!!")
elif temp>=20 and temp<=30:
    print("Cold Days!!")
elif temp>=10 and temp<=20:
    print("Too Cold!!")
else:
    print("Freeze!!")