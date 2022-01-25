from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')

snake= []
for turtle in range(3):
    Andy = Turtle(shape='square')
    Andy.color('white')
    Andy.penup()
    Andy.setposition(x=0-turtle*20, y=0)
    snake.append(Andy)










screen.exitonclick()