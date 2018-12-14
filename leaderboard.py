"""File to add leaderboard funktions to Mastermind"""

import json
from operator import itemgetter
import graphics as g


def create_window():
    """Create leaderboard window"""

    lb_window = g.GraphWin("score", 200, 400)
    return lb_window

def clear(win):
    """Cleans the leaderboard window"""
    for item in win.items[:]:
        item.undraw()
    win.update()

def show_lb(scores, lb_window):
    """Shows the leaderboard"""

    over_text = g.Text(g.Point(100, 50), "Score   name")

    player1 = str(scores[0]["score"]) + "     " + scores[0]["name"]
    player1p = g.Text(g.Point(100, 100), player1)

    player2 = str(scores[1]["score"]) + "     " + scores[2]["name"]
    player2p = g.Text(g.Point(100, 150), player2)

    player3 = str(scores[2]["score"]) + "     " + scores[2]["name"]
    player3p = g.Text(g.Point(100, 200), player3)

    player4 = str(scores[3]["score"]) + "     " + scores[3]["name"]
    player4p = g.Text(g.Point(100, 250), player4)

    player5 = str(scores[4]["score"]) + "     " + scores[4]["name"]
    player5p = g.Text(g.Point(100, 300), player5)

    over_text.setSize(10)
    player1p.setSize(10)
    player2p.setSize(10)
    player3p.setSize(10)
    player4p.setSize(10)
    player5p.setSize(10)

    over_text.draw(lb_window)
    player1p.draw(lb_window)
    player2p.draw(lb_window)
    player3p.draw(lb_window)
    player4p.draw(lb_window)
    player5p.draw(lb_window)

def get_new_score_name():
    """gets the nane of the player to add to the highscore board"""

    name_window = g.GraphWin("Name", 200, 200)

    get_name = g.Text(g.Point(100, 80), "Name")
    click_conf = g.Text(g.Point(100, 120), "Click to continue")

    name_enter = g.Entry(g.Point(100, 100), 10)

    get_name.draw(name_window)
    click_conf.draw(name_window)
    name_enter.draw(name_window)

    name_window.getMouse()

    name = str(name_enter.getText())

    name_window.close()

    return name

def add_and_sort(scores, new_name, new_score):
    """Adds the new value to the higscore list and sorts them and removes lowest"""
    newlist = sorted(scores, key=itemgetter("score"), reverse=True)
    player6 = {"score":new_score, "name":new_name}

    newlist.append(player6)

    sorted_plus = sorted(newlist, key=itemgetter("score"), reverse=True)

    del sorted_plus[-1]

    return sorted_plus

def import_list():
    """read highscore list from file"""

    with open("HS_file.json", "r") as read_file:
        hs_list = json.load(read_file)

    return hs_list

def save_new(list_save):
    """Saved new highscore list to file"""
    with open("HS_file.json", "w") as write_file:
        json.dump(list_save, write_file)

def getscore(rounds):
    """Returns score based on rounds"""

    if rounds == 1:
        return 64
    if rounds == 2:
        return 32
    if rounds == 3:
        return 16
    if rounds == 4:
        return 8
    if rounds == 5:
        return 4
    if rounds == 6:
        return 2
    if rounds == 7:
        return 1
