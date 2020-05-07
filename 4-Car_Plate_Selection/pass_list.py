car_plates = []

# Releases a pass list of cars whose license plates are allowed on a particular day
# Kind of a good initiative to reduce traffic in countries like India :)

number = int(input('Enter number of Car Plates to be entered :'))
print('Enter all the car plate numbers (general form : AB1234) : ')
for i in range(number):
    temp = input('Plate Number ' + str(i+1) + ': ')
    car_plates.append(temp)

odd_days = ['MO', 'WE', 'FR']
even_days = ['TU', 'TH', 'SA']

today = input('Enter today\'s day (MOnday, TUesday, etc): ')
pass_list = []

for plate in car_plates:
    temp = int(plate[-1])
    if today in odd_days and temp % 2 != 0:
        pass_list.append(plate)
    elif today in even_days and temp % 2 == 0:
        pass_list.append(plate)
    elif today == 'SU':
        pass_list.append(plate)

print('The Pass_List is as follows : ')
print(*pass_list, sep='\n')
    