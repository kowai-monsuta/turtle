from turtle import *



bgcolor("black")
speed(300)

def draw_square(some_turtle,size):

    some_turtle.goto(0,0)

    for i in range (1,5):
        some_turtle.forward(size)
        some_turtle.right(90)
        
        
def draw_art():

    apple= Turtle()
    apple.shape("turtle")
    apple.color("yellow")
    apple.speed(100)
    apple.pensize(2)
    for i in range(1,37):
        draw_square(apple,200)
        apple.right(10)
    for i in range(1,37):
        draw_square(apple,400)
        apple.right(10)
    for i in range(1,37):
        draw_square(apple,600)
        apple.right(10)
    for i in range(1,37):
        draw_square(apple,800)
        apple.right(10)


draw_art()


def draw_cirlce(turtle_some):

    for i in range (3,5):
        turtle_some.back(200)
        turtle_some.right(90)

def draw_design():
    
    pie = Turtle()
    for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
        pie.speed(1000)
        pie.right(46)
        pie.pensize(2)
        
        pie.pencolor("blue")
        pie.circle(1000)
        pie.pencolor("red")
        pie.circle(500)
        pie.pencolor("white")
        pie.circle(750)


draw_design()

setup(500, 500)
Screen()
title("Turtle Keys")
move = Turtle()
showturtle()

move.pensize(5)
move.pencolor("white")
        
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
