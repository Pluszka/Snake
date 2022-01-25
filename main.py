from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)


def make_snake_bigger(amount_of_parts):
    start_snake = []
    for turtle in range(amount_of_parts):
        Andy = Turtle(shape='square')
        Andy.color('white')
        Andy.penup()
        Andy.setposition(x=0-turtle*20, y=0)
        start_snake.append(Andy)
    return start_snake

game_on = True
snake_len = []
snake_len += make_snake_bigger(3)
while game_on:
    screen.update()
    time.sleep(0.1)
    for sq in range(len(snake_len) - 1, 0, -1):
        new_x = snake_len[sq - 1].xcor()
        new_y = snake_len[sq - 1].ycor()
        snake_len[sq].setposition(new_x, new_y)
    first_sqx = snake_len[0].xcor()
    first_sqy = snake_len[0].ycor()
    snake_len[0].setposition(first_sqx + 20, first_sqy)








screen.exitonclick()