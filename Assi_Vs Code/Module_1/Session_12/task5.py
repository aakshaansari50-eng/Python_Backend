from functools import reduce

prices = input("Enter item prices separated by space: ")

prices = list(map(int, prices.split()))

total = reduce(lambda x, y: x + y, prices)

print("Total Bill:", total)