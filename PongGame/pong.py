from turtle import Turtle

class ball(Turtle):
    def __init__(self):
        super(ball, self).__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.penup()
        self.xmove = 10
        self.ymove = 10

    def move(self):
        x = self.xcor() + self.xmove
        y = self.ycor() + self.ymove
        self.goto(x,y)

    def bounce(self):
        self.ymove *= -1

    def bounce2(self):
        self.xmove *= -1

    def reposition(self):
        self.goto(0,0)
        self.ymove = 10
        self.bounce2()

    def speedup(self):
        self.ymove *= 1.2