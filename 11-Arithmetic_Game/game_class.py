import random
import os
import time as t


def calculate(op1, op2, operator):
    if operator == '+':
        return op1 + op2
    elif operator == '-':
        return op1 - op2
    elif operator == '*':
        return op1 * op2
    else:
        return op1 % op2


class Game:
    number_of_questions = 0
    correct_answers = 0
    level = 0
    min_range = 0
    max_range = 0

    def __init__(self, number_of_ques, level):
        self.number_of_questions = number_of_ques
        self.level = level

    def lets_play(self):
        print("                    Let's begin the play!!...\n                    There will be ",
              self.number_of_questions, "number of questions.")
        if self.level == 1:
            self.min_range = 1
            self.max_range = 30
        elif self.level == 2:
            self.min_range = 20
            self.max_range = 50
        else:
            self.min_range = 40
            self.max_range = 70

        for i in range(self.number_of_questions):
            operand_1 = random.randint(self.min_range, self.max_range)
            operand_2 = random.randint(self.min_range, self.max_range)
            operator = random.choice(['+', '-', '*', '%'])
            print("\n                    What is ", operand_1, " ", operator, " ", operand_2, " = ?")
            user_answer = int(input("\n                    Your answer : "))
            actual_ans = calculate(operand_1, operand_2, operator)
            if user_answer == actual_ans:
                self.correct_answers += 1
            os.system('clear')

    def declare_results(self):
        print("                    Calculating results", end='')
        for j in range(3):
            print('.', end='', flush=True)
            t.sleep(1.0)
        if self.correct_answers > self.number_of_questions//2:
            text = "Well Done!"
        else:
            text = "Can do better"
        print("\n\n                    ", text)
        print("                    Correct answers : ", self.correct_answers, "\n                    Wrong answers : ",
              (self.number_of_questions - self.correct_answers))
