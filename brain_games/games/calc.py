# -*- coding:utf-8 -*-

"""Calculate Game logic."""

import operator
from random import choice, randint

GAME_RULES = 'What is the result of the expression?'


def make_round():
    """Run a round of Calculate Game.

    Returns:
        question: string with random operation between two integers 0-100
        correct_answer: result of the operation from question
    """
    rand_num1 = randint(0, 100)
    rand_num2 = randint(0, 100)
    sub_op = ('-', operator.sub)
    add_op = ('+', operator.add)
    mul_op = ('*', operator.mul)
    rand_op, function = choice([sub_op, add_op, mul_op])
    correct_answer = str(function(rand_num1, rand_num2))
    question = ('{0} {1} {2}'.format(rand_num1, rand_op, rand_num2))
    return question, correct_answer
