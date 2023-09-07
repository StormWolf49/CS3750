#Name: Nikhil Kowdle
#This program draws a picture with the turtle.

#Imports various resources to to be used in the program, as well as initializing it.
import turtle
from tkinter import * 
from PIL import Image
wd, ht = 500, 500
turtle.setup(width=wd, height=ht, startx=0, starty=0)
turtle.colormode(255)
t = turtle.Turtle()
t.speed(0)
colors = ['turquoise', 'tomato', 'lime green', 'dark orange', 'cornflower blue', 'fuchsia']

#Sets the background of the drawing in a way that will be saved in the postscript.
def draw_background(a_turtle):
    """ Draw a background rectangle. """
    ts = a_turtle.getscreen()
    canvas = ts.getcanvas()
    height = ts.getcanvas()._canvas.winfo_height()
    width = ts.getcanvas()._canvas.winfo_width()

    turtleheading = a_turtle.heading()
    turtlespeed = a_turtle.speed()
    penposn = a_turtle.position()
    penstate = a_turtle.pen()

    a_turtle.penup()
    a_turtle.speed(0)  # fastest
    a_turtle.goto(-width/2-2, -height/2+3)
    a_turtle.fillcolor(turtle.Screen().bgcolor())
    a_turtle.begin_fill()
    a_turtle.setheading(0)
    a_turtle.forward(width)
    a_turtle.setheading(90)
    a_turtle.forward(height)
    a_turtle.setheading(180)
    a_turtle.forward(width)
    a_turtle.setheading(270)
    a_turtle.forward(height)
    a_turtle.end_fill()

    a_turtle.penup()
    a_turtle.setposition(*penposn)
    a_turtle.pen(penstate)
    a_turtle.setheading(turtleheading)
    a_turtle.speed(turtlespeed)

#Creates a hexagon with a gradient from the white center to the black border, simulating a light diffusing down a hexagonal hallway.
def light():
    for i in range(0, 255, 3):
        t.penup()
        t.home()
        
        t.forward(285-(3*(i/3)))
        t.left(90)
        t.pencolor((i, i, i))
        t.fillcolor((i, i, i))
        t.begin_fill()
        t.pendown()
        t.circle(285-(3*(i/3)), steps=6)
        t.end_fill()

    t.penup()
    t.home()

#Creates a hexgaonal hallway by creating multiple conentric hexagons each slightly larger than the last, with each side being a different color.
def tunnel():
    for i in range(7):
        t.pencolor(colors[i%6])
        t.forward(300)
        t.penup()
        t.setposition(0, 0)
        t.pendown()
        t.left(60)
    
    t.penup()
    t.home()
    for i in range(400):
        if i%6 == 0:
            t.penup()
            t.home()
            t.forward(i)
            t.left(90)
            t.pendown()
        
        t.pencolor(colors[i%6])
        t.width(1)
        t.circle((i//6)*6, extent=60, steps=1)

    t.penup()
    t.home()
    t.forward(15)
    t.left(90)
    t.pencolor('white')
    t.fillcolor('white')
    t.begin_fill()
    t.pendown()
    t.circle(15, steps=6)
    t.end_fill()

#Creates a glowing golden orb at the end of the hallway, by creating a gradient golden circle with a white circle at the center of the gradient.
def orb():
    t.penup()
    t.home()

    for i in range(5):
        g = 215 + (i*8)
        b = i*51
        t.penup()
        t.home()
        t.forward(10-i)
        t.left(90)
        t.pencolor((255, g, b))
        t.fillcolor((255, g, b))
        t.begin_fill()
        t.pendown()
        t.circle(10-i)
        t.end_fill()

    t.penup()
    t.home()

#Executes the various drawing functions.
def main():
    turtle.bgcolor('black')
    draw_background(t)
    light()
    tunnel()
    orb()
    t.home()
    t.hideturtle()
    turtle.done()

main()