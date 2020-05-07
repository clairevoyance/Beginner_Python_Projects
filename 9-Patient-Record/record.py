# This program takes from the clerk a dictionary of all the patients in their records
# and then takes in the input of the persons standing in the queue....
# It then shows the patients whom they know so that they can give preference to them for treatment
# This is a basic program .....so please don't criticise its motive.....
# It is just to learn how dictionaries work


def print_it(a_list, a_dict):
    for person in a_list:
        for patient, info in a_dict.items():
            if person == patient:
                print(person + ':')
                for key, value in info.items():
                    print(key + '=' + str(value))
                print()


patients = {}

number = int(input('Enter the number of patients in your record : '))
for i in range(number):
    patient_info = {}
    nm = input('Enter patient Name : ')
    a = int(input('Enter Patient Age : '))
    w = int(input('Enter Patient Weight : '))
    patient_info.update({'age': a})
    patient_info.update({'weight': w})
    patients.update({nm: patient_info})

queue_list = []

num = int(input('Enter the number of persons in the queue : '))
for i in range(num):
    name = input('Enter the person name : ')
    queue_list.append(name)

print('The following persons are known to you : ')
print_it(queue_list, patients)
