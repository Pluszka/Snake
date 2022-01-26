from turtle import Turtle

MOVE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.start_snake = []
        self.startSnake()
        self.head = self.start_snake[0]

    def startSnake(self):
        for turtle in range(3):
            andy = Turtle(shape='square')
            andy.color('white')
            andy.penup()
            andy.setposition(x=0 - turtle * 20, y=0)
            self.start_snake.append(andy)

    def move(self):
        for sq in range(len(self.start_snake) - 1, 0, -1):
            new_x = self.start_snake[sq - 1].xcor()
            new_y = self.start_snake[sq - 1].ycor()
            self.start_snake[sq].setposition(new_x, new_y)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
