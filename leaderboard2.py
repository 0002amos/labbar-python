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

def show_lb(highscore, lb_window):
    """Shows the leaderboard"""

    over_text = g.Text(g.Point(100, 50), "Score   name")
    over_text.setSize(10)

    players_on_board =[]

    hight = 100         #Used to set the hight of scores
    
    list_to_sort = []

    for key, value in highscore.items(): #Transfer from dict to list to sort
        list_to_sort.append({"score": value, "name": key})
    
    list_sorted = sorted(list_to_sort, key=itemgetter("score"), reverse=True)   #sort the list 

    for i in range(len(list_sorted)):  #prepare the printing of top 5 players
        player = str(list_sorted[i]["score"]) + "     " + list_sorted[i]["name"]
        player_point = g.Text(g.Point(100, hight), player)
        player_point.setSize(10)
        players_on_board.append(player_point)
        hight += 50
    
    over_text.draw(lb_window)
    
    for i in range(len(players_on_board)): #print players to board 
        players_on_board[i].draw(lb_window)
        if i == 4:
            break
            #To stop it from writing more then 5 poeple to the board. Cant be added(to my knowledge) as a condition
            #to the loop since it can be shorten then 5 and then in range(5) gives errors

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

def add_score(highscore, new_name, new_score):
    """Adds the new value to the higscore list and sorts them and removes lowest"""

    if (new_name in highscore):
        highscore[new_name] = highscore[new_name] + new_score
    
    else:
        highscore[new_name] = new_score

    return highscore

def import_list():
    """read highscore list from file"""

    with open('data.txt') as json_file:  
        highscore = json.load(json_file)

    return highscore

def save_new(list_save):
    """Saved new highscore list to file"""
    with open('data.txt', 'w') as outfile:  
        json.dump(list_save, outfile)

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

