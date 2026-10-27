def calculate_total(price, quantity):
    return price * quantity

price=int(input("Enter Price: "))
quantity=int(input("Enter Quantity: "))
print(calculate_total(price, quantity))