# Ainur
# 11/14/23

# Draws hexagon shape

import turtle


screen = turtle.Screen()
screen.bgcolor("white")


pen = turtle.Turtle()
pen.speed(2)
pen.color("blue")
pen.pensize(2)

def draw_hexagon():
    for _ in range(6):
        pen.forward(50)
        pen.left(60)

for _ in range(9):
    draw_hexagon()
    pen.penup()
    pen.left(45)
    pen.pendown()

turtle.done()
