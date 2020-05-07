import os
import time as t
import game_class

# Menu Driven Arithmetic Game. Play as you like!

while True:
    os.system('clear')
    print("                     --------MENU--------  \n")
    print("                  1. Level 1")
    print("                  2. Level 2")
    print("                  3. Level 3")
    print("                  4. Exit this Hell!\n")
    choice = input("                  Enter your choice : ")

    if choice == '1':
        new_game = game_class.Game(3, 1)
        os.system('clear')
        new_game.lets_play()
        new_game.declare_results()
        print("                    Returning back to menu", end='')
        for j in range(3):
            print('.', end='', flush=True)
            t.sleep(1.0)

    elif choice == '2':
        new_game = game_class.Game(4, 2)
        os.system('clear')
        new_game.lets_play()
        new_game.declare_results()
        print("                    Returning back to menu", end='')
        for j in range(3):
            print('.', end='', flush=True)
            t.sleep(1.0)

    elif choice == '3':
        new_game = game_class.Game(5, 3)
        os.system('clear')
        new_game.lets_play()
        new_game.declare_results()
        print("                    Returning back to menu", end='')
        for j in range(3):
            print('.', end='', flush=True)
            t.sleep(1.0)
    elif choice == '4':
        break

    else:
        print("\nPlease enter a valid choice.....")
        os.system('clear')
