group_list = []

# To print the school numbers having maximum average of marks obtained by the students.

number_of_schools = int(input('Enter the number of schools : '))
for i in range(number_of_schools):
    number_of_students = int(input('Enter number of students in school ' + str(i+1) + ': '))
    temp_list = []
    for j in range(number_of_students):
        temp = int(input('Enter marks obtained by Student ' + str(j+1) + ' '))
        temp_list.append(temp)
    group_list.append(temp_list)


average_list = []

for school in group_list:
    total = 0
    for marks in school:
        total += marks
    average_list.append(total/(len(school)))

max_average_list = []
max_average = 0.0
for i in range(len(group_list)):
    if average_list[i] > max_average:
        max_average_list.clear()
        max_average_list.append(i+1)
        max_average = average_list[i]
    elif average_list[i] == max_average:
        max_average_list.append(i+1)

print('The school numbers having maximum average are/is : ')
print(*max_average_list, sep='\n')
print('The average of each school is : ', max_average)
