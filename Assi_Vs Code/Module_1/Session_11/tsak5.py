def update_cart(cart, item, qty):
    cart.update({item: qty})
    return cart


cart = {
    "T-Shirt": 2,
    "Shoes": 1
}

cart = update_cart(cart, "Jeans", 3)
print(cart)

cart = update_cart(cart, "T-Shirt", 5)
print(cart)