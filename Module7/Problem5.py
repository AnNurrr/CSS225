# Ainur
# 11/13/23
# Draws square inside square several times using turtle


import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for _ in range(4):
        t.forward(sz)
        t.left(90)

def drawNestedSquares(t, num_squares, initial_size, size_increment):
    """Draw nested squares using the drawSquare function"""
    for _ in range(num_squares):
        drawSquare(t, initial_size)
        initial_size += size_increment

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

num_squares = 5
initial_size = 20
size_increment = 20

# Draw the nested squares
drawNestedSquares(alex, num_squares, initial_size, size_increment)

wn.exitonclick()

