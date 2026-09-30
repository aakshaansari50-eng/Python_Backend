
# l=[]
# ev=[]
# od=[]
# n=int(input("Enter a Number : "))
# for i in range(1,n+1):
#     l.append(i)
#     if i%2==0:
#         ev.append(i)
#     else:
#         od.append(i)

# print(l)
# print(ev)
# print(od)




# l=[1,2,3,1,2]
# uni=[]
# dup=[]
# for i in l:
#     if i not in uni:
#         uni.append(i)
#     else:
#         dup.append(i)


# print(uni)
# print(dup)


l=[56,32,24,16,21] 
l.sort()

print("Sorted List is: ",l)
print("Smallest Element is: ",l[0])
print("Largest Element is: ",l[-1])
print("Second Smallest Element is: ",l[1])  
print("Second Largest Element is: ",l[-2])
