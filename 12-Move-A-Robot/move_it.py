import random

# import time as t
# import os

# This program intends to write all the steps taken by a robot to move from one point to the other
# It intends to teach basic operations of file handling in python

# We will be creating a file which will contain the specified moves as L, R, U, D
# and the robot will move accordingly

list_of_moves = ['L', 'R', 'U', 'D']

with open("moves.txt", "w") as file:
    for i in range(20):
        file.write(random.choice(list_of_moves))
        file.write(' ')
    file.close()


with open("moves.txt", "r") as file:
    data = file.readlines()
    for line in data:
        move = line.split(sep=' ')
        print(*move, sep=' ')
    file.close()

# Entering initial coordinates x and y
initial_x, initial_y = [int(x) for x in input("Enter the initial coordinates(separated by a space) : ").split()]

for direction in move:
    if direction == 'L':
        initial_x -= 1
    elif direction == 'R':
        initial_x += 1
    elif direction == 'U':
        initial_y += 1
    elif direction == 'D':
        initial_y -= 1

print("The final coordinates of the robot will be : ", initial_x, initial_y)
