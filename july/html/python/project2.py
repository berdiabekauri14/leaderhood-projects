from turtle import *

speed(30)
bgcolor('black')

color('dark blue')
begin_fill()

def earth(x, y):
    penup()
    goto(x, y)
    pendown()

    circle(100)

earth(190, 5)
end_fill()

color('blue')
def write_earth(x, y):
    penup()
    goto(x, y)
    pendown()

    write('Earth', align='center', font=('Arial', 30, 'normal'))

write_earth(100, 1)

color('gray')
begin_fill()

def moon(x, y):
    penup()
    goto(x, y)
    pendown()

    circle(50)

moon(-200, 1)
end_fill()

color('white')
def write_moon(x, y):
    penup()
    goto(x, y)
    pendown()

    write('Moon', align='center', font=('Arial', 30, 'normal'))

write_moon(-200, -50)

color('yellow')
begin_fill()

def sun(x, y):
    penup()
    goto(x, y)
    pendown()

    circle(900)

sun(-700, 1)
end_fill()

color('yellow')
def write_sun(x, y):
    penup()
    goto(x, y)
    pendown()

    write('Sun', align='center', font=('Arial', 30, 'normal'))

write_sun(-300, 50)

exitonclick()