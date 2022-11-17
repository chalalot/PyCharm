# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: 1
# Author: Tran Tuan Trung
# Created date: 19/11/2022
# Last modified date: 19/11/2022

import turtle

win = turtle.Screen()# create a screen and a turtle
t = turtle.Turtle()
t.speed(10)

def draw_border():
    t.pensize(5) #setup customized pen
    t.pencolor("blue")
    t.penup()
    t.goto(-200,-100) #go to location to align the flag to center
    t.pendown()
    t.fillcolor("red")#fill color for the flag
    t.begin_fill()
    for i in range (2): #draw the flag with desired size
        t.forward(400)
        t.left(90)
        t.forward(200)
        t.left(90)
    t.end_fill()
def draw_star():
    t.pencolor("white")
    t.fillcolor("white")
    t.penup()
    t.goto(-35,-21) #aligning the star
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for i in range (3): #draw the first triangle
        t.forward(70)
        t.left(120)
    t.goto(35,21) #aligning the second triangle
    t.left(180)
    for i in range(3): #draw the second triangle
        t.forward(70)
        t.left(120)
    t.end_fill()
    t.hideturtle()

draw_border()
draw_star()
win.exitonclick()