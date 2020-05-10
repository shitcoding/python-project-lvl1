# -*- coding:utf-8 -*-

"""Brain Games CLI printouts and prompts."""

import prompt


def greet_user():
    """Prompt `player_name`, print greeting.

    Returns:
        player_name: name entered by user.
    """
    player_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(player_name))
    return player_name


# Templates of dialog strings
QUESTION = 'Question: {0}'


WRONG_ANSWER = "'{0}' is wrong answer ;(. Correct answer was '{1}'."


TRY_AGAIN = "Let's try again, {0}!"


CONGRATS = 'Congratulations, {0}!'
