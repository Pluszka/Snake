from turtle import Turtle
import time
MOVE = 20

class Snake:

    def __init__(self):
        self.start_snake = []
        self.startSnake()
        self.head = self.start_snake[0]

    def startSnake(self):
        for turtle in range(3):
            Andy = Turtle(shape='square')
            Andy.color('white')
            Andy.penup()
            Andy.setposition(x=0 - turtle * 20, y=0)
            self.start_snake.append(Andy)


    def move(self):
        for sq in range(len(self.start_snake) - 1, 0, -1):
            new_x = self.start_snake[sq - 1].xcor()
            new_y = self.start_snake[sq - 1].ycor()
            self.start_snake[sq].setposition(new_x, new_y)
        self.head.forward(MOVE)

    def up(self):
        self.head.setheading(90)
        time.sleep(0.1)


    def down(self):
        self.head.setheading(270)
        time.sleep(0.1)

    def right(self):
        self.head.setheading(0)
        time.sleep(0.1)

    def left(self):
        self.head.setheading(180)
        time.sleep(0.1)
