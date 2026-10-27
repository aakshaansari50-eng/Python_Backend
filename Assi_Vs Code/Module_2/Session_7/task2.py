s = "Zomato gives tasty food and Zomato gives fast delivery".lower()
d = {}

for i in s.split():
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)