import turtle
from turtle import *
import time
from random import randint

turtle.setup(900, 900)
drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Catch The Mahmut")
mahmut = turtle.Turtle()

mahmut.shapesize(3)
mahmut.speed(0)
mahmut.shape('turtle')
mahmut.color("green")
mahmut.penup()


top_height = drawing_board.window_height()/2  # positive height/2 is the top of the screen
y = top_height - top_height/10  # decreasing a little bit so text will be visible
mahmut.setposition(0, y)
mahmut.write(arg='score:', move=True, align='center', font=("arial", 20, "normal"))




# hideturtle()
# write("SCORE", align="center", font=("Verdana", 15, "normal"))




def on_click():
    print()


mahmut.onclick(fun=on_click, btn=1)
while True:
    mahmut.goto(x=randint(-300, 300), y=randint(-300, 300))
    time.sleep(1)
