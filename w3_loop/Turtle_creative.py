import turtle

win = turtle.Screen()
win.bgcolor("black")
t = turtle.Turtle()
t.color("white")
t.speed(20)

def square():
    for i in range (4):
        t.forward(150)
        t.left(90)

def turn_left():
    t.left(5)

def turn_right():
    t.right(5)

def triagle():
    for i in range (3):
        t.forward(150)
        t.left(120)

def circle():
    t.circle(70)

for i in range (40):
    circle()
    turn_right()
t.penup()
t.left(90)
t.forward(140)
t.pendown()
for i in range (40):
    circle()
    turn_left()


win.exitonclick()