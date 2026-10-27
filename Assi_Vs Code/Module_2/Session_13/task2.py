songs = [[210, 180, 240], [150, 200], [300, 120, 90]]

l = [i for j in songs for i in j if i > 200]
print(l)