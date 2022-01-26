from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color('green')
        self.refresh()


    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-305, 280)
        self.setposition(x=rand_x, y=rand_y)