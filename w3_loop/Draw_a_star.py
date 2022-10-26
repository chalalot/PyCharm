import turtle

win = turtle.Screen()   # Set up a window
win.bgcolor("Red")  # Set up it's color
tito = turtle.Turtle()  # set up a turtle
tito.pensize(1)     # change it's pensize
tito.color("yellow")    # change it's color
tito.shape("blank")
tito.speed(10)
tito.left(72)
tito.fillcolor("Yellow")
tito.begin_fill()
tito.goto(-60,-60)
for i in range (1, 6):
    tito.forward(200)
    tito.right(144)
tito.end_fill()

win.exitonclick()