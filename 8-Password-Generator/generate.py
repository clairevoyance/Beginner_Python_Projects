import random
import time as t
import os

# As the name suggests, this program helps you to generate good passwords...if only u can remember those...lol :)

def get_char(char_list, number):
    temp_list = []
    for i in range(number):
        temp_list.append(random.choice(char_list))
    return temp_list


digit_list = [str(i) for i in range(0, 10)]
upper_list = [chr(i) for i in range(65, 65 + 26)]
lower_list = [chr(i) for i in range(97, 97 + 26)]
symbol_list = [chr(i) for i in range(32, 48)]
symbol_list += [chr(i) for i in range(58, 65)]
symbol_list += [chr(i) for i in range(91, 97)]
symbol_list += [chr(i) for i in range(123, 127)]
whole_list = digit_list + lower_list + upper_list + symbol_list

# taking user input
while True:
    num_char = int(input('Number of total characters : '))
    num_digit = int(input('Minimum Number of digits : '))
    num_upper = int(input('Minimum Number of uppercase characters : '))
    num_lower = int(input('Minimum Number of lowercase characters : '))
    num_symbol = int(input('Minimum Number of symbolic characters : '))
    if num_char < num_digit + num_lower + num_upper + num_symbol:
        print('Number of Characters does not match!')
    else:
        break

print('Calculating', end='')
for i in range(3):
    print('.', end='', flush=True)  # flush forcibly flushes the buffer to show the output
    t.sleep(1.0)

os.system('clear')
pass_digit = get_char(digit_list, num_digit)
pass_lower = get_char(lower_list, num_lower)
pass_upper = get_char(upper_list, num_upper)
pass_symbol = get_char(symbol_list, num_symbol)

remaining_char = num_char - num_lower - num_upper - num_digit - num_symbol
rem_list = get_char(whole_list, remaining_char)

password = pass_digit + pass_lower + pass_symbol + pass_upper + rem_list

random.shuffle(password)
password = ''.join(password)

print('\nGenerated Password is : ' + password + '\n')
