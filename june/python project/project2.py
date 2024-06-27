from turtle import *

import project2 as car

width(5)
speed(30)
color('red')
begin_fill()

penup()
goto(-100, 200)
pendown()

forward(200)
right(45)

forward(200)
left(-45)

forward(100)
right(90)

forward(50)
left(45)

forward(50)
right(90)

forward(50)
left(50)

forward(150)
left(45)

forward(50)
right(90)

forward(50)
left(45)

forward(50)
right(45)

forward(150)
left(-45)

forward(150)
right(90)

forward(200)
end_fill()

def window(x, y):
    penup()
    goto(x, y)
    pendown()

    width(7)
    color('aqua')
    begin_fill()

    forward(150)
    right(-45)

    forward(50)
    right(-50)

    forward(20)
    left(50)

    forward(50)
    left(50)

    forward(150)
    right(-90)

    forward(50)
    end_fill()

window(-50, 100)

def light(x, y):
    penup()
    goto(x, y)
    pendown()
    color('yellow')
    begin_fill()

    forward(30)
    left(90)

    forward(30)
    left(90)

    forward(30)
    left(90)

    forward(30)
    end_fill()

light(139, 120)

exitonclick()