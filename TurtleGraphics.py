# TurtleGraphics.py
# Name: Collin Frederick
# Date: 2/15/25
# Assignment:

import turtle 

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(myTurtle, sides, size=100):
    angle = 360 / sides
    for i in range(sides):
        myTurtle.forward(size)
        myTurtle.right(angle)

def fillCorner(myTurtle, size, corner):
  
    
    corner = 2
    corner = 3

    myTurtle.begin_fill()
    
    for i in range(4):
        myTurtle.forward(size)
        if i == corner - 2:  
            myTurtle.end_fill()
        myTurtle.right(90)
    
    myTurtle.end_fill()

def squaresInSquares(myTurtle, numSquares, size=50):

    for i in range(numSquares):
        drawSquare(myTurtle, size + (i * 20))  # Each square increases in size

def main():
    myTurtle = turtle.Turtle()
    myTurtle.speed(0)  # Speed up drawing
    


    drawPolygon(myTurtle, 5, 100)  # Draws a pentagon
    drawPolygon(myTurtle, 8, 100)  # Draws an octagon
    
    fillCorner(myTurtle, 100, 2)  # Draws a square with top right corner filled
    fillCorner(myTurtle, 100, 3)  # Draws a square with bottom left corner filled
    
    squaresInSquares(myTurtle, 5)  # Draws 5 concentric squares
    squaresInSquares(myTurtle, 3)  # Draws 3 concentric squares

turtle.done() 

main()
