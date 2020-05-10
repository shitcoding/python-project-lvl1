# -*- coding:utf-8 -*-

"""Greatest Common Divisor Game logic."""

from random import randint

GAME_RULES = 'Find the greatest common divisor of given numbers.'


def make_round():
    """Run a round of Greatest Common Divisor Game.

    Returns:
        question: 2 random integers 0-100
        correct_answer: greatest common divisor of these numbers
    """
    rand_num1, rand_num2 = (randint(0, 100), randint(0, 100))
    question = '{0} {1}'.format(rand_num1, rand_num2)
    a, b = (rand_num1, rand_num2)
    while a and b:   # Euclidean GCD calculation algorithm
        if a > b:
            a = a % b
        else:
            b = b % a
    correct_answer = str(a + b)
    return question, correct_answer
