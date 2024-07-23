from turtle import *

speed(30)
bgcolor('black')  

penup()
goto(-50, 60)
pendown()
color('blue')
begin_fill()
goto(100, 100)
goto(100, -100)
goto(-50, -60)
goto(-50, 60)
end_fill()

color('black')
width(10)
goto(15, 100)
goto(15, -100)

penup()
goto(100, 0)
pendown()
goto(-100, 0)

def text(x, y):
    penup()
    goto(x, y)
    pendown()

    color('white')

    write('Windows 10', align='center', font=('Arial', 30, 'normal'))

text(-200, 5)

exitonclick()