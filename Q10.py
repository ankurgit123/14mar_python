#Write a Python program to get unique values from a list

list_inp = [100, 75, 100, 20, 75, 12, 75, 25] 
set = set(list_inp)

print("The unique elements of the input list using set():") 

list=list(set)

for item in list:
    print(item)