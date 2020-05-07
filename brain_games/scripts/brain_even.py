# -*- coding:utf-8 -*-

"""Brain Even game script."""

from random import randint

import prompt

from brain_games import cli

GAME_RULES_STRING = 'Answer "yes" if number even otherwise answer "no".'


def main():
    """Brain Even game main function.

    Returns:
        is_victory: returns True if player won, False if player lost
    """
    cli.welcome_message()
    print(GAME_RULES_STRING, end='\n\n')
    player_name = cli.greet_user()
    player_correct_answers = 0
    while player_correct_answers < 3:
        random_int = randint(0, 1337)
        print('Question: {0}'.format(random_int))
        correct_answer = 'yes'
        if random_int % 2:
            correct_answer = 'no'
        player_answer = prompt.string('Your answer: ')
        if player_answer == correct_answer:
            player_correct_answers += 1
            print('Correct!')
        else:
            print("'{0}' is wrong answer ;(. ".format(player_answer), end='')
            print("Correct answer was '{0}'.".format(correct_answer))
            print("Let's try again, {0}!".format(player_name))
            return False
    print('Congratulations, {0}!'.format(player_name))
    return True


if __name__ == '__main__':
    main()
