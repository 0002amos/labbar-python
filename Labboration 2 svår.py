"""game mastermind"""
import random
import master_mind_GUI

def create_random():
    """Creates list of 4 letters"""
    target = [0, 0, 0, 0]
    for number in range(4):
        target[number] = random.randint(0, 5)
    print(target)
    return target


def check_right(target, guesses):
    """Checks right place and right color"""
    right_color = 0
    right_place = 0

    controll = target.copy()

    for i, color in enumerate(guesses):
        if target[i] == color:
            right_place += 1

        elif color in controll:
            controll.remove(color)
            right_color += 1

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

master_mind(create_random())
