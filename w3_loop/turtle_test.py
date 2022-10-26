import turtle
win = turtle.Screen()
win.bgcolor("pink")
tito = turtle.Turtle()
tess = turtle.Turtle()
tess.color("blue")
tess.pensize(5)

"""tito draws a square"""
tito.forward(150)
tito.left(90)
tito.forward(150)
tito.left(90)
tito.forward(150)
tito.left(90)
tito.forward(150)
tito.left(90)

"""tess draws an equilateral triangle"""
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)

win.exitonclick()