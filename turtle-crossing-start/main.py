import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from scoreboard import Scoreboard
score=Scoreboard()
car=CarManager()
player=Player()
STARTING_MOVE_DISTANCE = 5


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()
    score.update()
    for i in car.cars:
        if i.distance(player.p) < 15:
            score.over()
            game_is_on=False

        if player.p.ycor()==280:
            player.reset()
            score.increase()
            score.update()
            car.speed()
screen.exitonclick()



