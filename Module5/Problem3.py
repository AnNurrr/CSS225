# Ainur
# 11/1/2023
# Asks the user for polygon lengths, color, and prints that polygon

import turtle

number_sides = int(input("Enter number of sides of polygon: "))
length_sides = int(input("Enter length of each side: "))
color = input("Enter color: ")
color_fill = input("Enter fill color: ")

wn = turtle.Screen()

polygon = turtle.Turtle()

polygon.pencolor(color)
polygon.fillcolor(color_fill)
polygon.begin_fill()

for i in range(number_sides):
    polygon.forward(length_sides)
    polygon.right(360 / number_sides)

polygon.end_fill()

turtle.exitonclick()

wn.exitonclick()

