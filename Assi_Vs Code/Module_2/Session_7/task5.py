def char_count_dict(text):
    d = {}

    for i in text:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    return d


s = input("Enter Name: ").lower()
d = char_count_dict(s)

for i in sorted(d):
    print(i, ":", d[i])