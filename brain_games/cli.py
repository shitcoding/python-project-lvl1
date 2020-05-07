# -*- coding:utf-8 -*-

"""Brain Games script."""

import prompt


def welcome_message():
    """Print welcome message."""
    print('Welcome to the Brain Games!')  # noqa: WPS421


def greet_user():
    """Prompt `player_name`, print greeting.

    Returns:
        player_name: name entered by user.
    """
    player_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(player_name))  # noqa: WPS421
    return player_name
