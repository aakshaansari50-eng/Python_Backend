f = open("lyrics.txt", "r")

print(f.tell())

f.read(10)
print(f.tell())

f.close()