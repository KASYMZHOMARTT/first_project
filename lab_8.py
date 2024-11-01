# 1.1
# user_input = input("text: ")
# char_list = list(user_input.lower())
# print( char_list)

# 1.2
# user_list = input("text: ")
# vowels = "aeiou"
#
# list_vow = []
# list_cons = []
# list_sym = []
#
# for i in user_list:
#
#     if i in vowels:
#         list_vow.append(i)
#     elif i.isalpha():
#         list_cons.append(i)
#     else:
#         list_sym.append(i)
#
# print("list_vow:", list_vow)
# print("list_cons:", list_cons)
# print("list_sym:", list_sym)

 # 2.1
# name = input('Student name - ')
# ass = input('scores for assignments = ')
# tests = input('tests = ')
# labs = input('labs = ')
# student = {
#     'name':name,
#     'assignment':ass,
#     'test':tests,
#     'lab':labs,
# }
# print(student)

# 2.2
# name = input('Student name - ')
# ass = input('scores for assignments = ')
# tests = input('tests = ')
# labs = input('labs = ')
# student = {
#     'name':name,
#     'assignment':ass.split(','),
#     'test':tests.split(','),
#     'lab':labs.split(',')
# }
#
# count = len(student['assignment']) + len(student['test']) + len(student['lab'])
#
# student['name'] = count
# print(student)
# 2.3
# student = {
#     'name': 'Adam',
#     'assignment': [82, 56, 44, 30],
#     'test': [78, 77],
#     'lab': [78.2, 77.2]
# }
#
# count = len(student['assignment']) + len(student['test']) + len(student['lab'])
#
# if count >= 4:
#     avg_assignment = sum(student['assignment']) / len(student['assignment'])
#     avg_test = sum(student['test']) / len(student['test'])
#     avg_lab = sum(student['lab']) / len(student['lab'])
#
#     final_grade = 0.3 * avg_assignment + 0.5 * avg_lab + 0.2 * avg_test
# else:
#     final_grade = 0
#
# student['final_grade'] = round(final_grade, 2)
# print(student)
#
# students = [
#     {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2]},
#     {'name': 'Kevin', 'assignment': [82, 30], 'test': [], 'lab': [78.2]}
# ]
#
# rate = {}
# for student in students:
#     count = len(student['assignment']) + len(student['test']) + len(student['lab'])
#     rate[student['name']] = count
#
#     if count >= 4:
#         avg_assignment = sum(student['assignment']) / len(student['assignment']) if student['assignment'] else 0
#         avg_test = sum(student['test']) / len(student['test']) if student['test'] else 0
#         avg_lab = sum(student['lab']) / len(student['lab']) if student['lab'] else 0
#         final_grade = 0.3 * avg_assignment + 0.5 * avg_lab + 0.2 * avg_test
#     else:
#         final_grade = 0
#
#     student['final_grade'] = round(final_grade, 2)
#
# print("rate =", rate)
# for student in students:
#     print(student)

# 2.4
student1 = {
    'name': 'Adam',
    'assignment': [82, 56, 44, 30],
    'test': [78, 77],
    'lab': [78.2, 77.2],
    'final_grade': 70.25
}

student2 = {
    'name': 'Kevin',
    'assignment': [82, 30],
    'test': [],
    'lab': [78.2],
    'final_grade': 0
}

students = {
    student1['name']: {
        'assignment': student1['assignment'],
        'test': student1['test'],
        'lab': student1['lab'],
        'final_grade': student1['final_grade']
    },
    student2['name']: {
        'assignment': student2['assignment'],
        'test': student2['test'],
        'lab': student2['lab'],
        'final_grade': student2['final_grade']
    }
}

print(students)


