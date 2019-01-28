import graphics as g
import random

def createColors():
    """Create a 2D list of random colors"""

    colors = "Blue", "Green", "Yellow", "Red"
    color_list = []
    color_colum = []

    for i in range(15):
        color_colum = []
        for k in range(25):
            color_colum.append(random.choice(colors))
        color_list.append(color_colum)
    
    return color_list

def createGameWindow():
    """Create Both game and colorpick window"""
    gameWindow = g.GraphWin("game", 450, 800)

    return gameWindow

def createColorWindow():
    colorWindow = g.GraphWin("Color", 150, 500)
    return colorWindow

def createPickColor():
    """Create list with 4 colored squares to pick"""
    colorlist = []

    for i in range(50, 450, 100):
        point1 = g.Point(50, i)
        point2 = g.Point(100, i+50)
        shape = g.Rectangle(point1, point2)
        colorlist.append(shape)

    colorlist[0].setFill("Blue")
    colorlist[1].setFill("Green")
    colorlist[2].setFill("Yellow")
    colorlist[3].setFill("Red")

    return colorlist

def createGame(color_list):
    """Create 2D list of figures"""
    figurelist = []
    for i in range(0, 450, 30):
        figure_colum = []
        for k in range(0, 750, 30):
            point1 = g.Point(i,k)
            point2 = g.Point(i+30,k+30) 
            shape = g.Rectangle(point1, point2)
            colorRow = int(i/30)
            colorColum = int(k/30)
            shape.setFill(color_list[colorRow][colorColum])
            figure_colum.append(shape)
        figurelist.append(figure_colum)
    
    return figurelist

def drawGame(gameWindow, figurelist):
    """Draw the game on screen"""
    for i in range(15):
        for k in range(25):
            todraw = figurelist[i][k]
            todraw.draw(gameWindow)

def drawColorPick(colorPick, colorWindow):
    """Draw the 4 pick colors"""
    for i in range(4):
        colorPick[i].draw(colorWindow)

def updateWindow(gameWindow, figurelist, rounds):
    """Update the game window"""
    for item in gameWindow.items[:]:
        item.undraw()

    gameWindow.update()

    for i in range(15):
        for k in range(25):
            todraw = figurelist[i][k]
            todraw.draw(gameWindow)
    
    scoreText = str("Pick number:" + str(rounds))
    toPrint = g.Text(g.Point(100, 775), scoreText)

    toPrint.draw(gameWindow)

def updateFigure(figurelist, color_list):
    for i in range(15):
        for k in range(25):
            figurelist[i][k].setFill(color_list[i][k])

def pickColor(colorWindow, colorPick):
    """Allows input to be taken and return color"""
    picked = False
    while not picked:
        inputClick = colorWindow.getMouse()
        for i in range(4):
            sqr_to_check = colorPick[i]
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

    if ((X < 0) or (Y < 0) or (X > 14) or (Y > 24)):
        return

    if color_list[X][Y] != colorToChange:
        return

    color_list[X][Y] = newColor

    floodFill(X+1, Y, colorToChange, newColor, color_list)
    floodFill(X-1, Y, colorToChange, newColor, color_list)
    floodFill(X, Y+1, colorToChange, newColor, color_list)
    floodFill(X, Y-1, colorToChange, newColor, color_list)

def checkWin(colorlist):
    startcolor = colorlist[0][0]
    for i in range(15):
        for k in range(25):
            if colorlist[i][k] != startcolor:
                return False
    return True

def game():
    color_list = createColors()
    colorPick = createPickColor()
    gameWindow = createGameWindow()
    colorWindow = createColorWindow()
    figurelist = createGame(color_list)

    drawGame(gameWindow, figurelist)
    drawColorPick(colorPick,colorWindow)

    rounds = 1
    updateWindow(gameWindow, figurelist, rounds)

    playing = True

    lastColor = ""

    while playing:

        colorToSet = pickColor(colorWindow, colorPick)
        if ((colorToSet != lastColor) and colorToSet != (color_list[0][0])):
            floodFill(0, 0, color_list[0][0], colorToSet, color_list)
            rounds = rounds + 1
            updateFigure(figurelist,color_list)
            updateWindow(gameWindow, figurelist, rounds)

        lastColor = colorToSet

        if rounds == 50:
            playing = False
        
        if checkWin(color_list):
            playing = False
            print ("Du vann på", rounds-1, "rundor")

    gameWindow.getMouse()

game()