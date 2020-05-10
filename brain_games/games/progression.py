# -*- coding:utf-8 -*-

"""Progression game logic."""

from random import randint

GAME_RULES = 'What number is missing in the progression?'


def make_round():
    """Run a round of Progression game.

    Returns:
        progression: string, random arithmetic progression string
        correct_answer: string, number hidden from progression
    """
    num1 = randint(0, 100)
    step = randint(1, 10)
    hidden_index = randint(0, 9)
    progr_length = 0
    progression = ''
    while progr_length < 10:
        if progr_length == hidden_index:
            progression += '..' + ' '
            progr_length += 1
            correct_answer = str(num1)
            num1 += step
        else:
            progression += str(num1) + ' '
            progr_length += 1
            num1 += step
    return progression, correct_answer
