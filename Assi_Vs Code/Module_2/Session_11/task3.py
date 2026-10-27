import math

bill = float(input("Enter bill amount: "))
discount = bill * 10 / 100
total = bill - discount

print("Final Bill:", math.floor(total))