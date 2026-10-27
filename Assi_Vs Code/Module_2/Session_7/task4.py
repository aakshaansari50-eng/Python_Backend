s = input("Enter Review: ").lower()
stop = ["the", "and", "in", "of", "a", "to", "is"]
d = {}

for i in s.split():
    if i not in stop:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

print(d)