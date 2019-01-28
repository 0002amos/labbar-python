import graphics as g
import random
from leaderboard2 import *

def createColors():
    """Create a 2D list of random colors"""

    colors = "Blue", "Green", "Yellow", "Red"
    color_list = []
    color_colum = []

    for i in range(15): #Create 2D list of 15*25 with colors
        color_colum = []
        for k in range(25):
            color_colum.append(random.choice(colors))
        color_list.append(color_colum)
    
    return color_list

def createGameWindow():
    """Create Both game and colorpick window"""
    gameWindow = g.GraphWin("game", 450, 800) #Window to show game

    return gameWindow

def createColorWindow():
    """Create window for color pick"""
    colorWindow = g.GraphWin("Color", 150, 500) #Window to show colors to pick
    return colorWindow

def createPickColor():
    """Create list with 4 colored squares to pick"""
    color_list = []

    for i in range(50, 450, 100): #Create the 4 shapes to show colors
        point1 = g.Point(50, i)
        point2 = g.Point(100, i+50)
        shape = g.Rectangle(point1, point2)
        color_list.append(shape)

    #Set the right colors
    color_list[0].setFill("Blue")
    color_list[1].setFill("Green")
    color_list[2].setFill("Yellow")
    color_list[3].setFill("Red")

    return color_list

def createGame(color_list):
    """Create 2D list of figures"""
    figurelist = [] #2D list with figures
    for i in range(0, 450, 30):
        figure_colum = []
        for k in range(0, 750, 30):
            point1 = g.Point(i,k)
            point2 = g.Point(i+30,k+30) 
            shape = g.Rectangle(point1, point2)
            colorRow = int(i/30)
            colorColum = int(k/30)
            shape.setFill(color_list[colorRow][colorColum]) #Set color of figures to same as color list
            figure_colum.append(shape)
        figurelist.append(figure_colum)
    
    return figurelist

def drawGame(gameWindow, figurelist):
    """Draw the game on screen"""
    for i in range(15): #For loops to draw al figures to window
        for k in range(25):
            todraw = figurelist[i][k]
            todraw.draw(gameWindow)

def drawColorPick(colorPick, colorWindow):
    """Draw the 4 pick colors"""
    for i in range(4): #Draw the 4 colors
        colorPick[i].draw(colorWindow)

def updateWindow(gameWindow, figurelist, rounds):
    """Update the game window"""
    for item in gameWindow.items[:]:
        item.undraw() #Remove al elements in game window

    gameWindow.update() #update to ensure al is gone

    for i in range(15): #For loops to draw new figures
        for k in range(25):
            todraw = figurelist[i][k]
            todraw.draw(gameWindow)
    
    scoreText = str("Pick number:" + str(rounds)) #Show how many times a color has been picked(Shows 1 on first round)
    toPrint = g.Text(g.Point(100, 775), scoreText) #Create text to print

    toPrint.draw(gameWindow) #Draws text with rounds

def updateFigure(figurelist, color_list):
    """Uppdate the Figure list with the new colors"""
    for i in range(15): #For loops that update the 2D Figure lists colors to match 2D color list
        for k in range(25):
            figurelist[i][k].setFill(color_list[i][k])

def pickColor(colorWindow, colorPick):
    """Allows input to be taken and return color"""
    picked = False #False until choice is made
    while not picked:
        inputClick = colorWindow.getMouse() #gets input on where click has been made
        for i in range(4): #Runs all 4 choices to see if any match
            sqr_to_check = colorPick[i] #Compares to new square
            #Compares X and Y of square to see if click matches. If True square i has been clicked
            if sqr_to_check.p1.x < inputClick.x < sqr_to_check.p2.x and sqr_to_check.p1.y < inputClick.y < sqr_to_check.p2.y: 
                if i == 0: 
                    return "Blue"
                if i == 1:
                    return "Green"
                if i == 2:
                    return "Yellow"
                if i == 3:
                    return "Red"

def floodFill(X, Y, colorToChange, newColor, color_list):
    """Function to fill color list"""
    if ((X < 0) or (Y < 0) or (X > 14) or (Y > 24)): #Checks if we function tries to look outide of play area
        return

    if color_list[X][Y] != colorToChange: #If color on position is differant then what should change
        return

    color_list[X][Y] = newColor #Sets positions old color to the new one

    floodFill(X+1, Y, colorToChange, newColor, color_list) #To the left
    floodFill(X-1, Y, colorToChange, newColor, color_list) #To the right
    floodFill(X, Y+1, colorToChange, newColor, color_list) #Down
    floodFill(X, Y-1, colorToChange, newColor, color_list) #Up

def checkWin(color_list):
    """Checks if all colors are same as position [0][0]"""
    startcolor = color_list[0][0] #Saves color of [0][0] to variable for easy access
    for i in range(15):
        for k in range(25):
            if color_list[i][k] != startcolor: #If any color is not same as color on [0][0] stop and return False since game is not won
                return False
    return True #If all colors are the same as [0][0] the game ahs been won and return Tture

def game():
    """The game it self"""
    color_list = createColors() #Calls function to create 2D list of colors for game window
    colorPick = createPickColor() #Calls function to create list for colors to pick
    gameWindow = createGameWindow() #Calls function to create game window
    colorWindow = createColorWindow() #Calls funkcion to create color window
    figurelist = createGame(color_list) #Calls function to create 2D list with positions

    drawGame(gameWindow, figurelist) #Calls function to draws the game on game window
    drawColorPick(colorPick,colorWindow) #Calls function to draw window to pick colors

    rounds = 1 #Sets round to 1 for the first round
    updateWindow(gameWindow, figurelist, rounds) #Update window to ensure it is show right

    playing = True #Bool that is true whiles game is running

    lastColor = "" #String to remember what color was last picked 

    while playing: #Loop that is the game

        colorToSet = pickColor(colorWindow, colorPick) #Gets color from color pick window
        if ((colorToSet != lastColor) and colorToSet != (color_list[0][0])):
            #Checks if the picked color is the same as picked last round and if it is the same as on position [0][0] to avoid picking the same on round 1
            floodFill(0, 0, color_list[0][0], colorToSet, color_list) #Calls floodfill function to update list of colors
            rounds = rounds + 1
            updateFigure(figurelist,color_list) #Update figure list with new color list
            updateWindow(gameWindow, figurelist, rounds) #Update window with new list
            
            if checkWin(color_list): #Calls function to see if game is won
                playing = False
                #Save score to a new list with the old scores score is 100 devided by rounds/2 and rounded to 2 decimals
                new_list = add_score(import_list(), get_new_score_name(), round(100/(rounds/2), 3))
                gameWindow.getMouse() #waits for click and then closes al windows
                gameWindow.close()
                colorWindow.close()
                return new_list #Returns new list to save

        lastColor = colorToSet #Change last color

    gameWindow.getMouse() #To avoid unintended skips

def meny():
    """Print the meny and allow choice"""
    #Creates MENY texts and draws it
    meny = g.GraphWin("Meny", 200, 300)
    menyText = g.Text(g.Point(100,25), "MENY")
    menyText.setSize(15)
    menyText.draw(meny)
    
    #Creates PLAY text and bar and draws it
    playText = g.Text(g.Point(100, 75), "PLAY")
    playBar = g.Rectangle(g.Point(25, 60), g.Point(175, 90))
    playText.setFill("White")
    playBar.setFill("black")
    playText.setSize(15)
    playBar.draw(meny)
    playText.draw(meny)
    
    #Creates LEADERBOARD text and bar and draws it
    lbText = g.Text(g.Point(100, 125), "LEADERBOARD")
    lbBar = g.Rectangle(g.Point(25, 110), g.Point(175, 140))
    lbText.setFill("White")
    lbBar.setFill("Black")
    lbText.setSize(15)
    lbBar.draw(meny)
    lbText.draw(meny)
    
    #Creates QUIT text and bar and draws it
    quitText = g.Text(g.Point(100, 175), "QUIT")
    quitBar = g.Rectangle(g.Point(25, 160), g.Point(175, 190))
    quitText.setFill("White")
    quitBar.setFill("Black")
    quitText.setSize(15)
    quitBar.draw(meny)
    quitText.draw(meny)

    #Turns to True if any of the ones are clicked
    play = False 
    leaderboard = False
    quitGame = False

    while not quitGame:
        selection = meny.getMouse()
        #Checks if play was clicked
        if playBar.p1.x < selection.x < playBar.p2.x and playBar.p1.y < selection.y < playBar.p2.y:
            play = True
            picked = True
        #Checks if Leaderboard was clicked
        if lbBar.p1.x < selection.x < lbBar.p2.x and lbBar.p1.y < selection.y < lbBar.p2.y:
            leaderboard = True
            picked = True
        #Checks if quit was clicked
        if quitBar.p1.x < selection.x < quitBar.p2.x and quitBar.p1.y < selection.y < quitBar.p2.y:
            quitGame = True
            picked = True

        if play: #If play was clicked run the game and show leaderboard when won
            NEW_BOARD = game()
            LB_WIN = create_window()
            show_lb(NEW_BOARD, LB_WIN)
            save_new(NEW_BOARD)
            play = False
            LB_WIN.getMouse()
            LB_WIN.close()

        if leaderboard: #If leaderboard was clicked show leaderboard untill board is clicked
            LB_WIN = create_window()
            show_lb(import_list(), LB_WIN)
            LB_WIN.getMouse()
            LB_WIN.close()
            leaderboard = False
    
        if quitGame: #If quit was clicked turn program off
            return

meny() #Runs the whole game