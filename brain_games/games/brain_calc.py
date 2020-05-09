# -*- coding:utf-8 -*-

"""Brain Calculate game logic."""

import operator
from random import randint

from brain_games import cli

# Game settings.
GAME_RULES = 'What is the result of the expression?'
N_ANSWERS_TO_WIN = 3
OPS = {         # Operations to use in the game
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def brain_calc_round(n_answers_to_win, player_name='User'):
    """Run a round of Brain Calc game.

    Parameters:
        n_answers_to_win: Number of correct answers to win.
        player_name: Name entered by user, 'User' by default.

    Returns:
        True if player won,
        False if player lost
    """
    while n_answers_to_win:
        rand_num1, rand_num2 = (randint(0, 100), randint(0, 100))
        rand_op = list(OPS)[randint(0, len(OPS) - 1)]
        print('Question: {0} {1} {2}'.format(rand_num1, rand_op, rand_num2))
        correct_answer = OPS[rand_op](rand_num1, rand_num2)
        player_answer = cli.prompt.integer('Your answer: ')
        if player_answer == correct_answer:
            print('Correct!')
            n_answers_to_win -= 1
        else:
            print("'{0}' is wrong answer".format(str(player_answer)), end=' ')
            print(";(. Correct answer was '{0}'.".format(str(correct_answer)))
            print("Let's try again, {0}!".format(player_name))
            return False
    print('Congratulations, {0}!'.format(player_name))
    return True


def main():
    """Brain Calculate game main function."""
    cli.welcome_message(GAME_RULES)
    player_name = cli.greet_user()
    brain_calc_round(N_ANSWERS_TO_WIN, player_name)


if __name__ == '__main__':
    main()
