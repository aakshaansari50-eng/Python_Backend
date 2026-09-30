products = input("Enter product names separated by space: ")

products = products.split()

result = list(filter(lambda x: x.startswith("M"), products))

print("Products starting with M:", result)