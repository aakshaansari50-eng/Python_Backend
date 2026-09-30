def vowel(s,count=0):
    
    for i in s:
        if i in 'aeiouAEIOU':
            count+=1
    print("Total Vowels are : ", end="")        
    return count

s=input("Enter a String : ")
print(vowel(s))