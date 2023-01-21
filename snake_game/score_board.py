from turtle import Turtle
ALINE = "center"
FONT =("Arial", 20, "normal")
class Scoreboard(Turtle):
    def __init__(self):
       super().__init__()
       self.score =0
       self.color("white")
       self.penup()
       self.goto(0, 270)
       self.write(f"Score : {self.score}",align= ALINE,font=FONT)
       self.hideturtle()
       self.updatescore()

    def updatescore(self):
        self.write(f"Score : {self.score}",align= "center",font=("Arial", 20, "normal"))

    def gameover(self):
        self.color("white")
        self.goto(0,0)
        self.write("Game Over" , align= ALINE, font=FONT)

    def Score1(self):
        self.clear()
        self.score += 1
        self.updatescore()
