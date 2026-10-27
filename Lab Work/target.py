# # output target=9

# l=[5,2,11,2]
# target=9
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==target:
#             print([l,j])
#             break
#         else:
#             continue
#     break




l = [2, 7, 11, 15]
target = int(input("Enter the target: "))

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] + l[j] == target:
            print([i, j])
            
print("not found")


        
    
