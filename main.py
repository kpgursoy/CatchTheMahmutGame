import turtle
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

t1 = turtle.Turtle()
t1.hideturtle()
t1.penup()
t1.color("blue")

t2 = turtle.Turtle()
t2.hideturtle()
t2.penup()
t2.color("black")


def timer_board():
    timer = 20
    while timer > 0:
        t1.clear()
        top_height = drawing_board.window_height() / 2
        timer_y = top_height - top_height / 6
        t1.setposition(0, timer_y)
        t1.write(arg=f"timer : {timer}", move=True, align='center', font=("arial", 20, "normal"))
        timer -= 1

        mahmut.goto(x=randint(-300, 300), y=randint(-300, 300))
        time.sleep(1)

    t1.clear()
    t1.write(arg="Time's up!", move=True, align='center', font=("arial", 20, "normal"))


def score_board():
    top_height = drawing_board.window_height() / 2
    y = top_height - top_height / 10
    t2.setposition(0, y)
    t2.write(arg='score:', move=True, align='center', font=("arial", 20, "normal"))


score_board()
timer_board()


def update_score(x, y, current_score=0):
    current_score += 1
    top_height = drawing_board.window_height() / 2
    y = top_height - top_height / 10
    t2.setposition(0, y)
    # Clear the previous score display
    t2.write(arg=f'score: {current_score}', move=True, align='center', font=("arial", 20, "normal"))


mahmut.onclick(update_score)
