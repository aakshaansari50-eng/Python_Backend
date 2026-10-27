def word_freq_dict(s):
    d = {}

    for i in s.split():
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
        
    return d


s ="Zomato gives tasty food and Zomato gives fast delivery".lower()
print(word_freq_dict(s))