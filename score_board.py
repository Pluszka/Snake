from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Rockwell", 15, 'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.color('#F2E2D2')
        self.prompt()

    def prompt(self):
        self.clear()
        self.write(f'Current Score: {self.score}    High Score: {self.highest_score}', align=ALIGNMENT, font=FONT)

    def updateScore(self):
        self.score += 1
        self.prompt()

    def reset_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.score = 0
        self.prompt()
