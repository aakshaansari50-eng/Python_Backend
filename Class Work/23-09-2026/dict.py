# without bulit in method convert in dict
# l=[1,2,3]
# l1=[5,6,7]
# d={}
# for i in range(len(l)):
#     d[l[i]]=l1[i]

# print(d)



# d={} # convert a cube or square
# for i in range(1,31):
#     d[i]=i*i*i
    
# print(d)
       
# s=input("Enter Name : ".lower()) # count a name latter
# d={}

# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
        
# print(d)


d={'p':400,'q':100,'r':250} # addition of key and values
d1={'p':200,'q':100}

for i in d1:
    if i in d:  
        d[i]+=d1[i]
    else:
        d[i]=d1[i]
print(d)

# d={'p':400,'q':100,'r':250} # addition of key and values
# d1={'p':200,'q':100}
# ans={}
# for i,j in d.items():
#     for k,l in d1.items():
#         if i==k:
#             ans[i]=j+l
#         if i not in ans:
#             ans[i]=j
# print(ans)
        




        
