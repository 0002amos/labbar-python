"""game mastermind"""
import random
import master_mind_GUI

def create_random():
    """Creates list of 4 letters"""
    target = []
    target = (random.sample(range(0, 5), 4))
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
            playing = False

        if rounds == 7:
            master_mind_GUI.gameover_screen(rounds, "Looser")
            playing = False
            
master_mind(create_random())
