# -*- coding:utf-8 -*-

"""Even game logic."""

from random import randint

GAME_RULES = 'Answer "yes" if number is even, otherwise answer "no".'


def make_round():
    """Run a round of Even game.

    Returns:
        question: random integer from 0 to 1337,
        correct_answer: 'yes' if random_int is even, 'no' if odd
    """
    random_int = randint(0, 1337)
    correct_answer = 'yes'
    if random_int % 2:
        correct_answer = 'no'
    return random_int, correct_answer
