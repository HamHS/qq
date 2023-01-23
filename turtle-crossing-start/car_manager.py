from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager():

    def __init__(self):
        self.all = []
        self.speed = STARTING_MOVE_DISTANCE

    def carmake(self):
        randommake = random.randint(1,6)
        if randommake == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            car.penup()
            newy = random.randint(-250,250)
            car.setpos(300, newy)
            self.all.append(car)

    def car_move(self):
        for i in self.all:
            i.backward(self.speed)


    def levelup(self):
        self.speed += MOVE_INCREMENT