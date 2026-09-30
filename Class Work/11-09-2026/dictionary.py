d={1:"hello",2:"world",3:"python"}
print(d)

print(d.copy()) #copy of dictionary
print(d.get(2)) #get value of key 2 
print(d.items()) #get all items of dictionary

print(d.keys()) #get all keys of dictionary

print(d.values()) #get all values of dictionary

d.update({4:"java",5:"javascript"})#update dictionary
print(d)

d.pop(2) #remove key 2 from dictionary
print(d)

d.popitem() #remove last item from dictionary
print(d)

t=(1,2,3) #convert tuple to dictionary

d1={}

print(d1.fromkeys(t,"hello")) #create dictionary from tuple keys
