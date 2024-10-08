import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars=[]
        self.create_car()

    def create_car(self):
        n=random.randint(1,6)
        if n==1:

            c=Turtle()
            c.shape("square")
            c.shapesize(stretch_wid=1,stretch_len=2)
            c.color(random.choice(COLORS))
            c.penup()
            y=random.randint(-250,250)
            c.goto(300,y)
            self.cars.append(c)
    def move(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)
    def speed(self):
        global MOVE_INCREMENT
        for car in self.cars:
            car.backward(MOVE_INCREMENT)
        MOVE_INCREMENT=MOVE_INCREMENT+5
        print(MOVE_INCREMENT)












