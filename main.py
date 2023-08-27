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


def timer_board():
    t1 = turtle.Turtle()
    t1.color("blue")
    t1.penup()
    t1.hideturtle()
    top_height = drawing_board.window_height() / 2
    timer_y = top_height - top_height / 6
    t1.setposition(0, timer_y)
    t1.write(arg='timer:', move=True, align='center', font=("arial", 20, "normal"))


def score_board():
    t2 = turtle.Turtle()
    t2.color("black")
    t2.penup()
    t2.hideturtle()
    top_height = drawing_board.window_height() / 2
    score_y = top_height - top_height / 10
    t2.setposition(0, score_y)
    t2.write(arg='score:', move=True, align='center', font=("arial", 20, "normal"))


score_board()
timer_board()


while True:
    mahmut.goto(x=randint(-300, 300), y=randint(-300, 300))
    time.sleep(1)
