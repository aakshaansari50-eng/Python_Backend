l=[1,2,"apple",12.65,True,"banana",False,3.14,5,"grape"]
print(type(l))

l.append("orange") # Adds "orange" to the end of the list
print(l)

print("Count ele :",l.count(1)) # Counts the occurrences of 1 in the list

l.extend([600,700,800]) # Extends the list by adding elements from another list
print(l)

l.insert(2,"kiwi") # Inserts "kiwi" at index 2
print(l)

l.pop(3) # Removes and returns the element at index 3
print(l)

l.remove('orange') # Removes the first occurrence of 1 from the list
print(l)

l.clear()
print(l)

# l=[2,4,5,7,1] #sort not work as bollean values
# print(l)

# l.sort()
# print(l)


