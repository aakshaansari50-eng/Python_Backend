
# t=(1,2,"a","b",3.5,4.5,1)
# print("Type of t is: ",type(t))

# print(t.count(1))
# print(t.index("a"))



t=(1,2,"a","b",3.5,4.5,1)

l1=list(t)

l1.append(100)
print(l1)

t=tuple(l1)

print(t)