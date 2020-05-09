# -*- coding:utf-8 -*-

"""Brain Even game logic."""

from random import randint

from brain_games import cli, game_settings

GAME_RULES = 'Answer "yes" if number even otherwise answer "no".'


def brain_even_round(n_answers_to_win, player_name='User'):
    """Run a round of Brain Even game.

    Parameters:
        n_answers_to_win: Number of correct answers to win.
        player_name: Name entered by user, 'User' by default.

    Returns:
        True if player won,
        False if player lost
    """
    while n_answers_to_win:
        random_int = randint(0, 1337)
        print('Question: {0}'.format(random_int))
        correct_answer = 'yes'
        if random_int % 2:
            correct_answer = 'no'
        player_answer = cli.prompt.string('Your answer: ')
        if player_answer == correct_answer:
            n_answers_to_win -= 1
            print('Correct!')
        else:
            print("'{0}' is wrong answer ;(. ".format(player_answer), end='')
            print("Correct answer was '{0}'.".format(correct_answer))
            print("Let's try again, {0}!".format(player_name))
            return False
    print('Congratulations, {0}!'.format(player_name))
    return True


def main():
    """Brain Even game main function."""
    cli.welcome_message(GAME_RULES)
    player_name = cli.greet_user()
    brain_even_round(game_settings.n_answers_to_win, player_name)


if __name__ == '__main__':
    main()
