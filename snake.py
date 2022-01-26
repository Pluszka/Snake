from turtle import Turtle

class Snake:

    def __init__(self):
        self.start_snake = []
        self.startSnake()


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
        first_sqx = self.start_snake[0].xcor()
        first_sqy = self.start_snake[0].ycor()
        self.start_snake[0].setposition(first_sqx + 20, first_sqy)
