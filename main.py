from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=650)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)
player_score = 0

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
#TODO detect colision with food
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        player_score +=1

screen.exitonclick()
