import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.carmake()
    car.car_move()


    if player.ycor() > 280 :
        player.restart()
        score.score()
        car.levelup()

    for i in car.all:
        if i.distance(player) < 20:
            score.over()
            game_is_on = False

screen.exitonclick()