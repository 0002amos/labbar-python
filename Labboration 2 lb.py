"""game mastermind"""
import random
import master_mind_GUI
from leaderboard import *

def create_random():
    """Creates list of 4 letters"""
    target = []
    target = (random.sample(range(0, 6), 4))
    target = [1, 2, 3, 4]
    return target

def check_right(target, guesses):
    """Checks right place and right color"""
    right_color = 0
    right_place = 0

    check = []
    for position in range(4):
        if guesses[position] == target[position]:
            right_place += 1
            check.append(guesses[position])

    for position in range(4):
        if ((guesses[position] not in check) and (guesses[position] in target)):
            right_color += 1
            check.append(guesses[position])

    return (right_place, right_color)

def master_mind(target):
    """The game"""
    game_window = master_mind_GUI.create_GUI()

    rounds = 0
    playing = True

    while playing:

        guesses = master_mind_GUI.make_guess(rounds, game_window)

        right_wrong = check_right(target, guesses)

        master_mind_GUI.peg_feedback(rounds, right_wrong[0], right_wrong[1], game_window)
        rounds += 1

        if guesses == target:
            master_mind_GUI.gameover_screen(rounds, "Winner")

            score = getscore(rounds)

            new_list = add_and_sort(import_list(), get_new_score_name(), score)

            return new_list

        if rounds == 7:
            master_mind_GUI.gameover_screen(rounds, "Looser")
            playing = False

LB_WIN = create_window() #questionable constant
show_lb(import_list(), LB_WIN)

NEW_BOARD = master_mind(create_random())
clear(LB_WIN)

show_lb(NEW_BOARD, LB_WIN)
save_new(NEW_BOARD)

LB_WIN.getMouse()
