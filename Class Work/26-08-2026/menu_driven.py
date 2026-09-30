while True:
    menu="""
    press 1 for fibo series
    press 2 for prime number
    press 3 for Rev number
    press 4 for right pattern
    press 5 for left pattern
    press 6 for triange
    press 7 for exit
"""
    print(menu)
    choice=int(input("Enter Choice :"))

    if choice==1:
        n=int(input("Enter Terms :"))
        n1=0
        n2=1

        print(n1)
        print(n2)

        for i in range(3,n+1):
            n3=n1+n2
            print(n3)
            n1=n2
            n2=n3

    elif choice==2:
        n=int(input("Enter Number :"))
        prime=0

        for i in range(1,n+1):
            if(n%i==0):
                prime+=1

        if(prime==2):
            print("Prime Numner!!")
        else:
            print("Not a Prime Number!!")

    elif choice==3:
        n=int(input("Enter Number :"))
        rem=0
        rev=0
        n1=n

        while(n!=0):
            rem=n%10
            rev=rev*10+rem
            n//=10

            print(rev)

    elif choice==4:
        pass

    elif choice==7:
        print("Thank you")
        break

    else:
        print("Invalid Choice")
        break