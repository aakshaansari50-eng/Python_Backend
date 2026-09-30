def get_discounted_price(price, discount_percent):
    discount = price * discount_percent / 100
    final_price = price - discount
    return final_price


price=float(input("Enter the price of the product: "))
discount=float(input("Enter the discount percentage: "))
print("Final Price:", get_discounted_price(price, discount))