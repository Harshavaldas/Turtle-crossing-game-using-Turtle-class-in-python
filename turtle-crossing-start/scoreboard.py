from turtle import Turtle,Screen
FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.s=Turtle()
        self.score=0
        self.s.color("Black")
        self.s.penup()
        self.s.goto(x=0, y=260)
        self.s.hideturtle()
    def update(self):
        self.s.write(f"Level:{self.score}", align="center", font=("Courier", 24, "normal")

                     )
    def increase(self):
        self.score+=1
        self.s.clear()
        self.update()


    def over(self):
        self.s.goto(0,0)
        self.s.write("Game over",align="center",font=("Courier", 24, "normal"))


