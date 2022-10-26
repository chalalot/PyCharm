import turtle

win = turtle.Screen()
win.bgcolor("green")
t = turtle.Turtle()
t.color("blue")
l = turtle.Turtle()
l.color("blue")
t.shape("turtle")
l.shape("arrow")
t.pensize(5)
t.speed(1)
t.penup()
t.goto(0, -180)
t.pendown()
t.circle(180)
t.penup()

l.speed(1)
l.pensize(3)

t.goto(0,0)
for i in range (12):
    t.forward(150)
    t.stamp()
    t.back(150)
    t.right(30)
t.stamp()
for i in range (12):
    l.penup()
    l.forward(120)  #go to position
    l.pendown()
    l.forward(10)   #draw
    l.penup()
    l.back(130)     #go back
    l.right(30)     #rotate

win.exitonclick()