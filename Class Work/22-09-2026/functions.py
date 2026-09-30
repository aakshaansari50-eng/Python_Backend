"""def rev_no(): # Default Function
    no=int(input("Enter a Number : "))
    rev=0
    rem=0
    
    while(no!=0):
        rem=no%10
        rev=rev*10+rem
        no//=10
    print(rev)
rev_no()
"""
"""def rev_no(no,rem=0,rev=0): #  Function with para and with args
    rem=0
    rev=0
    while(no!=0):
        rem=no%10
        rev=rev*10+rem
        no//=10
    print(rev)
no=int(input("Enter a Number :"))    
rev_no(no)
"""

"""def rev_no():#  Function without para and with return type
    no=int(input("Enter a Number :"))
    rem=0
    rev=0
    while(no!=0):
        rem=no%10
        rev=rev*10+rem
        no//=10
    return rev
  
print(rev_no())
"""

def rev_no(no,rem=0,rev=0):#Function with para and with return type
    rem=0
    rev=0
    while(no!=0):
        rem=no%10
        rev=rev*10+rem
        no//=10
    return rev

no=int(input("Enter a Number :"))
print(rev_no(no))
