s=input("Enter a String : ")
count=0

for i in s:
    if i in 'aeiouAEIOU':
        count+=1
        
print("Total Vowels are : ",count)