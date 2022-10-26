import turtle
# set up a window and a turtle
win = turtle.Screen()
win.bgcolor("pink")
tito = turtle.Turtle()
tito.pensize(5)
tess =turtle.Turtle()
tess.pensize(10)
tito.shape("square")
tess.shape("turtle")
tito.speed(10)

for i in range (0, 12):
    tito.up()
    tito.forward(25)
    tito.down()
    tito.forward(25)
    tito.left(30)

tess.up()
for size in range (5, 60, 2):
    tess.stamp()
    tess.forward(size)
    tess.right(24)
win.exitonclick()