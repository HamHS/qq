
from turtle import Turtle
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.update()
        self.hideturtle()

    def update(self):
        self.goto(-200, 250)
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def score(self):
        self.level += 1
        self.clear()
        self.update()

    def over(self):
        self.goto(0,0)
        self.color("black")
        self.write("GAVE OVER", align= "center", font=FONT)