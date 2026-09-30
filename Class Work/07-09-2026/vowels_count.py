#vowels and consonants count using string
s=input("Enter a string :")
count=0
for i in s:
    if i in 'aeiouAEIOU':
        count+=1
print("Total Vowels are :",count)