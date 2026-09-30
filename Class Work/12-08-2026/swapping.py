#swapping

# with using third variable


#a=100 b=50

#temp=a #temp=100 a=blank
#a=b #a=50 a=blank
#b=temp #b=100 temp=blank

#a=a+b #100+50 a=150
#b=a-b #150-50=100
#a=a-b #150-100=50

# without using third variable

a=int(input("Enter Number for A :"))
b=int(input("Enter Number for B :"))

a,b=b,a

print("Before Swapping A",a)
print("After Swapping B",b)