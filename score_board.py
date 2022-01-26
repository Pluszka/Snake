import turtle
from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0,300)
        self.color('white')
        self.write(f'Current Score: {self.score}', align='center',font=("Rockwell", 15, 'bold'))