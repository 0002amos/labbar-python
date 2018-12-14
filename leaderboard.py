from operator import itemgetter
from master_mind_GUI import *
import graphics as g

LBwindow = g.GraphWin("score",200 ,400)

def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

def show_lb(scores):
    
    clear(LBwindow)

    over_text = Text(Point(100,50),"Score   name")
    score1 = str(scores[0]["score"])
    name1 = scores[0]["name"]
    player1 = score1 +"     " + name1
    player1p = Text(Point(100, 100), player1)

    score2 = str(scores[1]["score"])
    name2 = scores[1]["name"]
    player2 = score2 +"     " + name2
    player2p = Text(Point(100, 150), player2)

    score3 = str(scores[2]["score"])
    name3 = scores[2]["name"]
    player3 = score3 +"     " + name3
    player3p = Text(Point(100, 200), player3)
    
    score4 = str(scores[3]["score"])
    name4 = scores[3]["name"]
    player4 = score4 +"     " + name4
    player4p = Text(Point(100, 250), player4)

    score5 = str(scores[4]["score"])
    name5 = scores[4]["name"]
    player5 = score5 +"     " + name5
    player5p = Text(Point(100, 300), player5)

    over_text.setSize(10)
    player1p.setSize(10)
    player2p.setSize(10)
    player3p.setSize(10)
    player4p.setSize(10)
    player5p.setSize(10)

    over_text.draw(LBwindow)
    player1p.draw(LBwindow)
    player2p.draw(LBwindow)
    player3p.draw(LBwindow)
    player4p.draw(LBwindow)
    player5p.draw(LBwindow)


def get_new_score_name():
    name_window = g.GraphWin("Name",200, 200)

    get_name = Text(g.Point(100, 80), "Skriv ditt namn här")
    enter = Entry(g.Point(100,100), 5)

    enter.draw(name_window)
    
    name_window.getMouse()
    
    get_name.draw(name_window)
    drawtxt_ = enter.getText()
    
    return drawtxt_

def add_and_sort(scores, new_name, new_score):
    newlist = sorted(scores, key=itemgetter("score"), reverse=True)
    player6 = {"score":new_score, "name":new_name}
    
    newlist.append(player6)

    sorted_plus = sorted(newlist, key=itemgetter("score"), reverse=True)

    del sorted_plus[-1]

    return sorted_plus 

def import_list():

    player1 = {"score":2, "name":"A"}
    player2 = {"score":4, "name":"B"}
    player3 = {"score":5, "name":"C"}
    player4 = {"score":3, "name":"D"}
    player5 = {"score":2, "name":"E"}

    hs = [player1, player2, player3, player4, player5]

    return hs
#player6 = {"score":5, "name":"amos"}

show_lb(import_list())

show_lb(add_and_sort(import_list(), get_new_score_name(), 50))

LBwindow.getMouse()