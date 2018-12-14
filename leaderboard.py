from operator import itemgetter 
import graphics as g
import json

def create_window():
    LBwindow = g.GraphWin("score",200 ,400)
    return LBwindow

def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

def show_lb(scores, LBwindow):
    
    over_text = g.Text(g.Point(100,50),"Score   name")
    score1 = str(scores[0]["score"])
    name1 = scores[0]["name"]
    player1 = score1 + "     " + name1
    player1p = g.Text(g.Point(100, 100), player1)

    score2 = str(scores[1]["score"])
    name2 = scores[1]["name"]
    player2 = score2 + "     " + name2
    player2p = g.Text(g.Point(100, 150), player2)

    score3 = str(scores[2]["score"])
    name3 = scores[2]["name"]
    player3 = score3 + "     " + name3
    player3p = g.Text(g.Point(100, 200), player3)
    
    score4 = str(scores[3]["score"])
    name4 = scores[3]["name"]
    player4 = score4 + "     " + name4
    player4p = g.Text(g.Point(100, 250), player4)

    score5 = str(scores[4]["score"])
    name5 = scores[4]["name"]
    player5 = score5 + "     " + name5
    player5p = g.Text(g.Point(100, 300), player5)

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
    """
    get_name = g.Text(g.Point(100, 80), "Skriv ditt namn här")
    enter = g.Entry(g.Point(100,100), 5)
    
    get_name.draw(name_window)
    enter.draw(name_window)
    
    drawtxt_ = enter.getText()
    name_window.getMouse

    name_window.close()
    return drawtxt_
    """
    get_name = g.Text(g.Point(100,80), "Name")
    click_conf = g.Text(g.Point(100,120), "Click to continue")

    name_enter = g.Entry(g.Point(100, 100), 10)

    get_name.draw(name_window)
    click_conf.draw(name_window)
    name_enter.draw(name_window)

    name_window.getMouse()

    name = str(name_enter.getText())

    name_window.close()

    return (name)

def add_and_sort(scores, new_name, new_score):
    newlist = sorted(scores, key=itemgetter("score"), reverse=True)
    player6 = {"score":new_score, "name":new_name}
    
    newlist.append(player6)

    sorted_plus = sorted(newlist, key=itemgetter("score"), reverse=True)

    del sorted_plus[-1]

    return sorted_plus 

def import_list():

    with open("HS_file.json", "r") as read_file:
        hs = json.load(read_file)

    return hs

def save_new(list_save):
    with open("HS_file.json", "w") as write_file:
        json.dump(list_save, write_file)

def getscore(rounds):
    if rounds == 1:
        return 64
    elif rounds == 2:
        return 32
    elif rounds == 3:
        return 16
    elif rounds == 4:
        return 8
    elif rounds == 5:
        return 4        
    elif rounds == 6:
        return 2
    elif rounds == 7:
        return 1

#player6 = {"score":5, "name":"amos"}

#show_lb(import_list())

#show_lb(add_and_sort(import_list(), get_new_score_name(), 50))

#LBwindow.getMouse()