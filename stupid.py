from turtle import *
import time

def draw_square(some_turtle, size):

    some_turtle.goto(0,0)

    for i in range (1,5):
        some_turtle.forward(size)
        some_turtle.right(90)
        
        
def draw_art(some_turtle):

    some_turtle.pensize(3)
    some_turtle.fillcolor("red")
    
    for i in range(1,37):
        draw_square(some_turtle, 50)
        some_turtle.right(10)
        some_turtle.pencolor("white")
    for i in range(1,37):
        draw_square(some_turtle, 100)
        some_turtle.right(10)
        some_turtle.pencolor("red")
    for i in range(1,37):
        draw_square(some_turtle, 200)
        some_turtle.right(10)
        some_turtle.pencolor("blue")
    for i in range(1,37):
        draw_square(some_turtle, 300)
        some_turtle.right(10)
        some_turtle.pencolor("yellow")
    for i in range(1,37):
        draw_square(some_turtle, 400)
        some_turtle.right(10)
        some_turtle.pencolor("white")
    for i in range(1,37):
        draw_square(some_turtle, 500)
        some_turtle.right(10)
        some_turtle.pencolor("red")
    for i in range(1,37):
        draw_square(some_turtle, 600)
        some_turtle.right(10)
        some_turtle.pencolor("blue")
    for i in range(1,37):
        draw_square(some_turtle, 700)
        some_turtle.right(10)
        some_turtle.pencolor("yellow")
    for i in range(1,37):
        draw_square(some_turtle, 800)
        some_turtle.right(10)
        some_turtle.pencolor("white")


def draw_design(some_turtle):
    pie.speed(1000)
    pie.pensize(2)

    for i in range(1,100):
        some_turtle.right(10)
        some_turtle.pencolor("blue")
        some_turtle.circle(100)
        some_turtle.pencolor("white")
        some_turtle.circle(50)
        some_turtle.pencolor("red")
        some_turtle.circle(75)
        some_turtle.pencolor("yellow")
        some_turtle.circle(25)

setup(500, 500)
title("Turtle Keys")

bgcolor("black")

time.sleep(10)

apple = Turtle()
apple.shape("turtle")
apple.color("white")
apple.speed(900)

pie = Turtle()

move = Turtle()
move.pensize(5)
move.pencolor("white")


draw_art(apple)
draw_design(pie)


pie.reset()
apple.reset()

     
def k1():
    move.forward(45)

def k2():
    move.left(45)

def k3():
    move.right(45)

def k4():
    move.back(45)

onkey(k1, "Up")
onkey(k2, "Left")
onkey(k3, "Right")
onkey(k4, "Down")


listen()
mainloop()

done()

