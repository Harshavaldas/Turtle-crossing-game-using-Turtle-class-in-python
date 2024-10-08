STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player():
    def __init__(self):
        self.p=Turtle()
        self.p.shape("turtle")
        self.p.penup()
        self.p.goto(STARTING_POSITION)
        self.p.color("black")
        self.p.setheading(90)
    def move(self):
        self.p.forward(20)
    def reset(self):
        self.p.goto(0,-280)


