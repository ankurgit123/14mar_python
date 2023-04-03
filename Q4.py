#Write a Python program to get a single string from two given strings, separated by a space and swap the first
#two characters of each string. 

Str1=input("Enter name of first")
Str2=input("Enter name second")


Str1=Str1.replace(Str1[0:2], Str2[0:2])  #Replacing string first two letters with second string
Str2=Str2.replace(Str2[0:2], Str1)  # Replacing string2 first two letters with string 1

print(Str1)
print(Str2)