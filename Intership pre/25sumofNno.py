def sum_of_n_no(no,sum=0):
    for i in range(1,no+1):
        sum+=i
        print(i)
        
    print("Sum is :",end="")
    return sum

no=int(input("Enter a Number : "))
print(sum_of_n_no(no))