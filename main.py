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
    for sq in range(len(start) - 1, 0,-1):
        new_x = start[sq-1].xcor()
        new_y = start[sq - 1].ycor()
        start[sq].setposition(new_x, new_y)
    first_sqx = start[0].xcor()
    first_sqy = start[0].ycor()
    start[0].setposition(first_sqx+20, first_sqy)








screen.exitonclick()