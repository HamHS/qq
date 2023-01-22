from turtle import Turtle
ALINE = "center"
FONT =("Arial", 20, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.score2 = 0
        self.color("white")
        self.penup()
        self.updatescore()
        self.hideturtle()

    def updatescore(self):
        self.goto(-100, 200)
        self.write(f"{self.score}",align= "center",font=("Arial", 20, "normal"))
        self.goto(100, 200)
        self.write(f"{self.score2}",align= "center",font=("Arial", 20, "normal"))

    def Score1(self):
        self.clear()
        self.score += 1
        self.updatescore()

    def Score2(self):
        self.clear()
        self.score2 += 1
        self.updatescore()
