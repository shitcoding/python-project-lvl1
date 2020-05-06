# -*- coding:utf-8 -*-

"""Brain Games script."""

import prompt


def welcome_user():
    """Prompt name, print greeting."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))  # noqa: WPS421
