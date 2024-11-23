# Task 1
# Write a program that accepts two lists and outputs
# all the elements of the first one that are not in the second one.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# b = list(set(a) - set(b))
# print("Екінші тізімде жоқ бірінші тізімнің элементтері:", b)

# Task 2
# Print a list of files in the specified directory.

# Task 3
# Add up the digits of an integer.

# n = input("Сан енгіз: ")
# sum = 0
# for i in n:
#     if i.isdigit():
#         sum += int(i)
#
# print("Сандардың қосындысы:", sum)

# Task 4
# Count the number of times a character occurs in a string.

# z = input("Сөйлем жаз: ")
# c = input("Санағың келетін әріп енгіз: ")
#
# count = z.count(c)
# print(f"{c} әріпі cөйлемде {count} рет кездеседі")

# Task 5
# Swap the values of the variables.
# a = input("a мәнін енгіз: ")
# b = input("b мәнін енгіз: ")
#
# temp = a
# a = b
# b = temp
#
# print(f"Алмасудан кейін: a = {a}, b = {b}")

# Task 6
# Use the anonymous function to extract numbers divisible by 15 from the list.

# numbers = [15, 30, 22, 45, 10, 60, 33, 90]
#
# divisible_by_15 = list(filter(lambda x: x % 15 == 0, numbers))
#
# print("15-ке бөлінетін сандар:", divisible_by_15)

# Task 7
# You need to check if all the numbers in the sequence are unique.

# numbers = input("Сандарды енгіз: ")
#
# unique = len(numbers) == len(set(numbers))
# if unique:
#     print("Барлық сандар бірегей")
# else:
#     print("Қайталанатын сандар бар")
