# -*- coding:utf-8 -*-

"""Main Brain Games script."""

from brain_games import cli


def main():
    """Print welcome message, ask for a name, greet user."""
    cli.welcome_message()
    cli.greet_user()


if __name__ == '__main__':
    main()
