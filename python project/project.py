import turtle

import project as logo

wn = turtle.Screen()
wn.bgcolor("black")

waveform = turtle.Turtle()
waveform.color("yellow")
waveform.speed(5)

def draw_waveform(turtle_obj):
    turtle_obj.penup()
    turtle_obj.goto(-200, 0)
    turtle_obj.pendown()
    turtle_obj.begin_fill()
    for _ in range(2):
        turtle_obj.left(90)
        turtle_obj.forward(50)
        turtle_obj.right(90)
        turtle_obj.forward(50)
        turtle_obj.right(90)
        turtle_obj.forward(50)
    turtle_obj.end_fill()

name = turtle.Turtle()
name.color("yellow")
name.speed(5)

def write_name(turtle_obj):
    turtle_obj.penup()
    turtle_obj.goto(0, -50)
    turtle_obj.pendown()
    turtle_obj.write("Berdia Bekauri", align="center", font=("Arial", 16, "normal"))

draw_waveform(waveform)

write_name(name)

waveform.hideturtle()
name.hideturtle()

wn.mainloop()