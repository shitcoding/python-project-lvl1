# -*- coding:utf-8 -*-

"""Brain Games script."""

import prompt


def welcome_message(game_rules):
    """Print welcome message and game rules.

    Parameters:
        game_rules: GAME_RULES of particular Brain Game to print.
    """
    print('Welcome to the Brain Games!')
    print(game_rules, end='\n\n')


def greet_user():
    """Prompt `player_name`, print greeting.

    Returns:
        player_name: name entered by user.
    """
    player_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(player_name))
    return player_name
