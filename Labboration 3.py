"""Labboration 3 del A"""

import math as m

import graphics as g

def start_triangle(side_lenght, middle, color, win):
    """Fuction to draw first triangle before remove of pieces"""
    vert_lenght = m.sqrt((side_lenght**2)-((side_lenght/2)**2))
    point1 = g.Point(middle.getX() - (side_lenght/2), middle.getY() + vert_lenght/2)    #Lower left
    point2 = g.Point(middle.getX() + (side_lenght/2), middle.getY() + vert_lenght/2)    #Lower right
    point3 = g.Point(middle.getX(), middle.getY() - vert_lenght/2)                     #Upper middle
    shape = g.Polygon(point1, point3, point2)
    shape.setFill(color)
    shape.draw(win)

def remove_triangle(side_lenght, middle, win):
    """Remove triangles to create a Sierpinski triangle"""

    if side_lenght <= 1:
        return

    vert_lenght = m.sqrt((side_lenght**2)-((side_lenght/2)**2))

    point1 = g.Point(middle.getX() - (side_lenght/4), middle.getY()) #Lower left
    point2 = g.Point(middle.getX() + (side_lenght/4), middle.getY()) #Lower Right
    point3 = g.Point(middle.getX(), middle.getY() + vert_lenght/2)   #Lower middle

    shape = g.Polygon(point1, point3, point2)
    shape.setFill("White")
    shape.draw(win)

    #Help for next part
    #           1
    #         2   3
    #       4       5
    #     6   7   8   9
 

    #To shorten argument for functions
    side_lenght = side_lenght/4                         #New side lenght to send into function
    X_point_5 = middle.getX() + side_lenght             #Set x för point 5
    X_point_4 = middle.getX() - side_lenght             #Set x för point 4
    x_point_2_7 = middle.getX() - side_lenght/2         #Set x för point 2 and 7
    x_point_3_8 = middle.getX() + side_lenght/2         #Set x for point 3 and 8
    yp_1_8 = middle.getY() + vert_lenght/8              #Set y for point 4 and 5
    Y_point_6_7_8_9 = middle.getY() + vert_lenght*3/8   #Set y for point 6, 7, 8 and 9

   #Here recursive cals are made for triangles around the one triangle that was just drawn

    remove_triangle(side_lenght, g.Point(middle.getX(), middle.getY() - vert_lenght/2*(3/4)), win)
    remove_triangle(side_lenght, g.Point(x_point_2_7, middle.getY() - vert_lenght/2*(1/4)), win)
    remove_triangle(side_lenght, g.Point(x_point_3_8, middle.getY() - vert_lenght/2*(1/4)), win)
    remove_triangle(side_lenght, g.Point(X_point_4, yp_1_8), win)
    remove_triangle(side_lenght, g.Point(X_point_5, yp_1_8), win)
    remove_triangle(side_lenght, g.Point(middle.getX() - side_lenght*1.5, Y_point_6_7_8_9), win)
    remove_triangle(side_lenght, g.Point(x_point_2_7, Y_point_6_7_8_9), win)
    remove_triangle(side_lenght, g.Point(x_point_3_8, Y_point_6_7_8_9), win)
    remove_triangle(side_lenght, g.Point(middle.getX() + side_lenght*1.5, Y_point_6_7_8_9), win)

def sierpinski(win, size, start, color):
    """Calls both start_triangle funktion and remove_triangle function at once"""
    start_triangle(size, start, color, win)
    remove_triangle(size, start, win)

#Start Window (Pylint says WIN but is no constant only named all Capital for 10/10 rating)
WIN = g.GraphWin("Sierpinski triangle", 900, 900)
#Change here to another window, size, start coordinates or color
sierpinski(WIN, 800, g.Point(450, 450), "Red")

WIN.getMouse()      #Wait with closing the window until click
WIN.close()         #Close window
