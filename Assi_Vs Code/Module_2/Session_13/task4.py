ratings = [[4, 5, 3, 2], [5, 4, 4, 3], [3, 2, 5, 5]]

l = [i for j in ratings for i in j if i > 4]
print(l)