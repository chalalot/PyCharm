import turtle

win = turtle.Screen()
win.bgcolor("black")
t = turtle.Turtle()
t.pensize(5)
t.speed(30)
def draw_a_square(t, size):
    for a_color in ["red", "green", "blue","pink"]:
        t.color(a_color)
        t.forward(size)
        t.left(90)
size = 20
for i in range (25):
    draw_a_square(t, size)
    size = size + 10
    t.forward(10)
    t.right(18)

win.exitonclick()