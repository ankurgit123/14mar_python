#Write a Python program to sort a dictionary (ascending /descending) by value.

y={'carl':40,'alan':2,'bob':1,'danny':3} 

l=list(y.list()) #convert the given dict. into list

l.sort()            #sort the list
print('Ascending order is',l) #this print the sorted list in ascending order

l=list(y.items())
l.sort(reverse=True) #sort in reverse order
print('Descending order is',l)

dict=dict(l) # convert the list in dictionary 

print("Dictionary",dict) #the desired output is this sorted dictionary