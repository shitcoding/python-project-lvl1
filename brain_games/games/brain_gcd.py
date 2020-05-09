# -*- coding:utf-8 -*-

"""Greatest Common Divisor game logic."""

from random import randint

from brain_games import cli, game_settings

GAME_RULES = 'Find the greatest common divisor of given numbers.'


def brain_gcd_round(n_answers_to_win, player_name='User'):
    """Run a round of Greatest Common Divisor game.

    Parameters:
        n_answers_to_win: Number of correct answers to win.
        player_name: Name entered by user, 'User' by default.

    Returns:
        True if player won,
        False if player lost
    """
    while n_answers_to_win:
        rand_num1, rand_num2 = (randint(0, 100), randint(0, 100))
        print('Question: {0} {1}'.format(rand_num1, rand_num2))
        a, b = (rand_num1, rand_num2)   # Euclidean GCD algorithm
        while a and b:
            if a > b:
                a = a % b
            else:
                b = b % a
        correct_answer = a + b
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
    """Greatest Common Divisor game main function."""
    cli.welcome_message(GAME_RULES)
    player_name = cli.greet_user()
    brain_gcd_round(game_settings.n_answers_to_win, player_name)


if __name__ == '__main__':
    main()
