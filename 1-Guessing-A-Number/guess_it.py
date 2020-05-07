import random as rd

play_game = 'y'

# This program intends to show the basic use of random function
# It predicts a number and ascertains it's position w.r.t the user-entered number to help the user get close to it's value

while play_game == 'y':
    answer = rd.randint(1, 100)
    user_input = input('Guess a number between 1 and 100 : ')
    user_input = int(user_input)
    if user_input == answer:
        print('Hurrah!! You have guessed it right ')
    else:
        counter = 1
        while user_input != answer:
            if user_input > answer:
                print('Try guessing a smaller number .')
            else:
                print('Try guessing a larger number .')
            # print(counter, ' tries left')
            counter += 1
            var = input('Let\'s try again, enter a value between 1 and 100 : ')
            user_input = int(var)
            if user_input == answer:
                print('Yeah you got it !!')
                print('You required ', counter, 'tries')
                break
    play_game = input('Do you want to replay this game? (y/n)')
