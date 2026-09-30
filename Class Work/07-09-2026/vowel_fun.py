def vowel(s,count=0):
    
    for i in s:
        if i in 'aeiouAEIOU':
            count+=1
    return count

s=input("Enter a string :")
print(vowel(s))

