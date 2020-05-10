# -*- coding:utf-8 -*-

"""Prime Number game logic."""

from random import randint

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_round():
    """Run a round of Prime Number game.

    Returns:
        rand_num: random integer 1-1000
        correct_answer: 'yes' if number is prime, otherwise 'no'
    """
    rand_num = randint(1, 1000)
    correct_answer = 'yes'
    for i in range(2, rand_num // 2):
        if (rand_num % i) == 0:
            correct_answer = 'no'
            break
    return rand_num, correct_answer
