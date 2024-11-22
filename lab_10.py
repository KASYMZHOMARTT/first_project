# Task 1
# Write a check to see if the string is a palindrome. A palindrome is a word or phrase that reads equally
# from left to right and from right to left.
#
# z = input("Сөз енгіз: ")
#
# x = z.replace(" ", "").lower()
#
# if x == x[::-1]:
#     print("Рас")
# else:
#     print("Жалған")

# Task 2
# Make the number of seconds appear as days:hours:minutes:seconds.
# seconds = int(input("Секунд: "))
#
# days = seconds // 86400
# hours = (seconds % 86400) // 3600
# minutes = (seconds % 3600) // 60
# second = seconds % 60
#
# print(f"{days} күн, {hours} сағат, {minutes} минут, {second} секунд")

# Task 3
# You accept from the user a sequence of numbers separated by a comma. Make a list and a tuple with these numbers.
# z = input("Үтірмен бөлінген сандарды енгіз: ")
#
# x = z.split(",")
# n = tuple(x)
#
# print("Тізім:", x)
# print("Кортеж:", n)

# Task 4
# Print the first and last item in the list.
#
# word = input("Сөз енгіз: ").split()
#
# print("Бірінші элемент:", word[0])
# print("Екінші элемент:", word[-1])

# Task 5
# Write a program that accepts the file name and outputs its extension.
# If the file extension cannot be determined, throw an exception.

# file_name = input("Файл атын енгіз: ")
#
# if "." in file_name:
#     print("Файл аты:", file_name.split(".")[-1])
# else:
#     print("Қате, файл табылмады")

# Task 6
# For a given integer n, count n + nn + nnn.
#
# n = input("Сан енгіз: ")
# nn = n + n
# nnn = n + n + n
#
# result = int(n) + int(nn) + int(nnn)
# print("Нәтиже:", result)

# Task 7
# Write a program that outputs even numbers from a given list and stops if it encounters the number 237.

# numbers = [12, 37, 56, 78, 237, 89, 90, 24, 36]
#
# for n in numbers:
#     if n == 237:
#         print(n)
#         break
#     if n % 2 == 0:
#         print(n)

