#sorting without using inbult function

# l=[66,52,78,16,21]
# for i in range(len(l)): #66 
#     for j in range(i+1,len(l)): # 52
#         if l[j]<l[i]: #52<66
#             temp=l[i] #66
#             l[i]=l[j] #52
#             l[j]=temp #66
        
# print("Sorted list is: ",l)



# reverse list without using inbuilt function
l=[56,32,24,16,21]
for i in range(len(l)):
    for j in range(i+1,len(l)):
       l[j],l[i]=l[i],l[j]
print("Reversed list is: ",l)