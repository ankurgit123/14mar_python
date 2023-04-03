#Write a python program to sum of the first n positive integers.

n = int(input("Enter a positive integer: "))
sum = 0

# Calculate the sum of the first n positive integers
for i in range(1, n+1):
    sum += i

print("The sum of the first positive integers is")
print(n)
print(sum)