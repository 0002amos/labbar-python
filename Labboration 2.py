import random
import master_mind_GUI

def create_random():
    target =[]
    target = (random.sample(range(0, 5), 4))
    return target

def check_right(target, guesses):
    right_color = 0
    right_place = 0

    check = []
    for a in range(4):
        if guesses[a] == target[a]:
            right_place += 1
            check.append(guesses[a])

    for a in range(4):
       if ((guesses[a] not in check) and (guesses[a] in target)):
           right_color += 1
           check.append(guesses[a])

    return (right_place, right_color)

def master_mind(target):

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

        if (rounds == 7):
            master_mind_GUI.gameover_screen(rounds, "Looser")

master_mind(create_random())   