#Write a Python program to check whether a list contains a sublist.

list1 = [1, 2, 3, 4, 5, 4, 5]

list2 = [4, 5, 6, 7, 8, 4, 5]

set1 = set(list1)

set2 = set(list2)

intersected_set = set1.intersection(set2)

intersected_list = list(intersected_set)

print(intersected_list)