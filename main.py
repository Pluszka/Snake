from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=650)
screen.bgcolor('#4D5057')
screen.title('Snake')
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.grow()
        score_board.updateScore()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 295 or snake.head.ycor() < -315:
        score_board.reset_score()
        snake.reset_snake()
    for segment in snake.start_snake[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset_score()
            snake.reset_snake()
screen.exitonclick()

