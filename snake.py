from turtle import Turtle
POSISTION =[(0,0),(-20,0),(-40,0)]
DISTANSE = 20
UP = 90
DOWUN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.segment = []
        self.creatSnake()
        self.head = self.segment[0]

    def creatSnake(self):
        for i in POSISTION:
            self.add_segment(i)

    def add_segment(self, position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.segment.append(tim)

    def expend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for i in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[i - 1].xcor()
            new_y = self.segment[i - 1].ycor()
            self.segment[i].goto(new_x, new_y)
        self.head.forward(DISTANSE)

    def up(self):
        if self.head.heading() != DOWUN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWUN)

    def right(self):
        if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() !=RIGHT:
            self.head.setheading(LEFT)
