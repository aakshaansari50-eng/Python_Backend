def rev_str(s,rev=" "):
    for i in s:
        rev=i+rev
    
    print("Reverse String : ",end="")    
    return rev

s=input("Enter a String : ")
print(rev_str(s))    