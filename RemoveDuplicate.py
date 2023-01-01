students =  ["Python", "R", "C#", "Python", "R", "Java"]
# # Using del method
# del students[3]
# print(students)

# # Using for Loop
# new_list = []
#
# for one_student_choice in students:
#     if one_student_choice not in new_list:
#         new_list.append(one_student_choice)
# print(new_list)

# # Using set
# new_list = list(set(students))
# print(new_list)

# Using Dictionary
list_of_tuples = list(map(lambda x: (x, None), students))
print(list_of_tuples, end = '\n\n')

dict_students = dict(list_of_tuples)

print('The resulting dictionary from the list of tuples:')
print(dict_students, end='\n\n')

new_list = list(dict_students.keys())

print('The new list without duplicates:')
print(new_list, end='\n\n')