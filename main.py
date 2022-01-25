from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)


def make_snake():
    start_snake = []
    for turtle in range(3):
        Andy = Turtle(shape='square')
        Andy.color('white')
        Andy.penup()
        Andy.setposition(x=0-turtle*20, y=0)
        start_snake.append(Andy)
    return start_snake

game_on = True
start = make_snake()
while game_on:
    screen.update()
    time.sleep(0.1)
    for sq in start:
        sq.forward(20)












screen.exitonclick()