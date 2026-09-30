import random

#lucky=random.randint(1,50)

#l=[123654799,25413689,58741369,8896547123]
#lucky=random.choice(l)
#print(lucky)

lucky=random.randint(1,51)

while True:
    
    choice=int(input("Enter your lucky number: "))
    
    if choice>50:
        print("Please enter a number between 1 to 50")
        break
        
    elif choice==lucky:
        print("Congratulations! You have won the lottery")
        break
    
    elif lucky>choice:
        print("Original number is bigger")
        
    else:
        print("Original number is smaller")
        