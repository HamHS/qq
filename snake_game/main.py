import turtle
from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
end = False


while end == False:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.expend()
        scoreboard.Score1()


    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        end = True
        scoreboard.gameover()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            end = True
            scoreboard.gameover()

screen.exitonclick()

