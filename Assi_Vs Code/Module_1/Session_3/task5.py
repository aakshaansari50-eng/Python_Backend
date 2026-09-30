num1=int(input("Enter Number 1 : "))
num2=int(input("Enter Number 2 : "))
operator=input("Enter Operator (+ , - , * , / ) :")

if operator == "+":
    print("Answer : ",num1+num2)

elif operator == "-":
    print("Answer : ",num1-num2)

elif operator == "*":
    print("Answer : ",num1*num2)

elif operator == "/":
    print("Answer : ",num1/num2)

else:
    print("Please used correct opeartor!!")