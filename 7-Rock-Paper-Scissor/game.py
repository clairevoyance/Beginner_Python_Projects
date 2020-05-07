import random
import time as t
import os

# It is kind of a game between computer and user regarding the most played game by 90s kids.... rock, paper, scissor

option_list = ['r', 'p', 's']
draw = 0
user_win = 0
user_lose = 0
prompt = 'Choose Rock(r) or Paper(p) or Scissor(s)...or Quit(q) : '
while True:
    user_input = input(prompt)
    if user_input == 'q':
        print('Number of Draws : ', draw)
        print('Number of User Wins : ', user_win)
        print('Number of User Losses : ', user_lose)
        t.sleep(2.0)
        print('Quitting...')
        t.sleep(2.0)
        break
    else:
        if user_input not in option_list:
            while user_input not in option_list:
                user_input = input(prompt)
        # computer's turn
        computer_input = random.choice(option_list)
        print('Computer chose : ' + computer_input)
        if computer_input == user_input:
            print('Its a Draw....')
            draw += 1
        elif computer_input == 'r':
            if user_input == 'p':
                print('You win this chance...')
                user_win += 1
            else:
                print('You lose this chance..')
                user_lose += 1
        elif computer_input == 'p':
            if user_input == 's':
                print('You win this chance...')
                user_win += 1
            else:
                print('You lose this chance..')
                user_lose += 1
        else:
            if user_input == 'r':
                print('You win this chance...')
                user_win += 1
            else:
                print('You lose this chance..')
                user_lose += 1
    t.sleep(2.0)
    os.system('clear')
