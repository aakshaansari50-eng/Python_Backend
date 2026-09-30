list=[1,2,3,1,2,5]
uni=[]
dup=[]
for i in list:
    if i not in uni:
        uni.append(i)
    else:
        dup.append(i)
        
print("Unique :",uni)
print("Duplicate :",dup)
