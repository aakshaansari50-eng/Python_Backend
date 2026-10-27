class A:
    def List(self):
        l=[56,61,45,32]
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                if l[j]<l[i]:
                    temp=l[i]
                    l[i]=l[j]
                    l[j]=temp
        print("Sorted List : ",l)
        
class B:
    def List(self):
        super().List()
        l=[32,41,16]
        l1=[65,54,21]
        d={}
        for i in range(len(l)):
            d[l[i]]=l1[i]
        print("Convert in Dictionary : " ,d)
        
class C(B,A):
    def List(self):
        super().List()
        l=[1,2,3,1,2]
        uni=[]
        for i in l:
            if i not in uni:
                uni.append(i)
        print("Unique List : ",uni)
               
obj=C()
obj.List()