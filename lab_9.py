# Task 1
# There is a list a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Print all the elements that are less than 5.
import operator

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for b in a:
#     if b<5:
#         print(b)

# Task 2
# The lists are given:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
# You need to return a list that consists of elements that are common to these two lists.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# b = list(set(a) & set(b))
# print(b)

# Task 3
# Sort the dictionary by value in ascending and descending order.
# Import the necessary module and declare the dictionary:
# import operator

# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# x = sorted(d.items(), key = operator.itemgetter(1))
# z = sorted(d.items(), key = operator.itemgetter(1), reverse=True)
#
# print(x)
# print(z)

# Task 4
# Write a program to merge several dictionaries into one.
# Let's say here are our dictionaries:

# dict_a = {1:10, 2:20}
# dict_b = {3:30, 4:40}
# dict_c = {5:50, 6:60}
#
# dict_x = {}
# for d in (dict_a, dict_b, dict_c):
#     dict_x.update(d)
#
# print(dict_x)

# Task 5
# Find the three keys with the highest values in the dictionary
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
#
# keys = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
# print(keys)

# Task 6
# Write a code that converts an integer into a string, despite the fact that it can be used in any number system.


# Task 7
# You need to print the first n lines of Pascal's triangle. In this triangle, there are units at the top and
# on the sides, and each number inside is equal to the sum of the two numbers above it.


