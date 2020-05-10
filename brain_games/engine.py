# -*- coding:utf-8 -*-

"""Games engine."""

from brain_games import cli, game_settings


def run(game):
    """Run a Brain Game.

    Parameters:
        game: particular game from ./brain_games/games/

    Returns:
        True if player won, False if player lost
    """
    print('Welcome to the Brain Games!')
    print(game.GAME_RULES)
    player_name = cli.greet_user()
    counter = game_settings.N_ANSWERS_TO_WIN
    while counter:
        question, correct_answer = game.make_round()
        print(cli.QUESTION.format(question))
        answer = cli.prompt.string('Your answer: ')
        if answer != correct_answer:
            print(cli.WRONG_ANSWER.format(answer, correct_answer))
            print(cli.TRY_AGAIN.format(player_name))
            return False
        counter -= 1
        print('Correct!')
    print(cli.CONGRATS.format(player_name))
    return True
