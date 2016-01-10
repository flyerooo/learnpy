import turtle
def drawGrid():
    turtle.penup()
    turtle.goto(-300, 250)
    turtle.pendown()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(300)
def drawColumns():
    for i in range(4):
        turtle.right(90)
        turtle.forward(37.5)
        turtle.right(90)
        turtle.forward(300)
        turtle.left(90)
        turtle.forward(37.5)
        turtle.left(90)
        turtle.forward(300)
def drawRows():
    turtle.left(180)
    rows = 0
    while rows <= 3:
        rows += 1
        turtle.forward(37.5)
        turtle.right(90)
        turtle.forward(300)
        turtle.left(90)
        turtle.forward(37.5)
        turtle.left(90)
        turtle.forward(300)
        turtle.right(90)
def main():
    drawGrid()
    drawColumns()
    drawRows()
main()
