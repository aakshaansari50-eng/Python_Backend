l=[14,12,78,37,2,1]
print("Original list :" ,l)
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[j]<l[i]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
    
print("Sorting : ",l)