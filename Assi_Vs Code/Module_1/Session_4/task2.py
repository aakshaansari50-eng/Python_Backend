marks=int(input("Enter Marks : "))

if marks >= 90:
    print("A+ Grade")
elif marks >= 75 and marks <= 89:
    print("B Grade")
elif marks >= 60 and marks <= 74:
    print("C Grade")
elif marks >= 40 and marks <= 59:
    print("D Grade")
else:
    print("Fail!!")