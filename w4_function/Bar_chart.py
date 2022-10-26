import turtle
win = turtle.Screen()
win.bgcolor("green")
t = turtle.Turtle()
t.color("blue")
t.pensize(3)
t.fillcolor("red")
t.penup()
t.goto(-200,-200)
t.pendown()
l = turtle.Turtle()
l.color("yellow")
l.pensize(3)
l.penup()
l.goto(-200,0)
l.shape("circle")
k = turtle.Turtle()
k.penup()
k.goto(-200,-200)
k.pencolor("black")
k.shape("arrow")
k.pensize(3)
def draw_a_bar(t, height):
    #start filling shape
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(height, font = ("Arial", 16, "bold"))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

l.pendown()

def line_graph(l, height,i):
    l.goto (i, height)
    l.stamp()

k.pendown()

def table_outline():
    k.forward(450)
    k.stamp()
    k.back(450)
    k.left(90)
    k.forward(450)
    k.stamp()

table_outline()

for height,i in [[123,-180],[76,-140],[154,-100],[201,-60],[13,-20],[65,20],[76,60],[154,100],[201,140],[205,180]]:
    line_graph(l, height, i)
    draw_a_bar(t, height)

win.exitonclick()