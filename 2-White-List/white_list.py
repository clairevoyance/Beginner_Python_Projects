black_list = ['Peter', 'Susan', 'Tanya', 'Victor']

white_list = []
stud_input = []

# To show all candidates not in the black list.

number = int(input('Enter the number of students : '))

for i in range(number):
    user_input = input('Enter a name : ')
    while user_input == '':
        user_input = input('Enter a non-empty name : ')
    stud_input.append(user_input)

for student in stud_input:
    if student not in black_list:
        white_list.append(student)
print('These', len(white_list), 'students are white listed : ')
print(*sorted(white_list), sep='\n')
