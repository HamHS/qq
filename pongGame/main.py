import time
from turtle import Screen
from Score import Scoreboard
from paddle import Paddle
from pong import ball

screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

score = Scoreboard()
paddle = Paddle((350,0))
paddle2 = Paddle((-350,0))
ball = ball()


screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

end = False

while end != True:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()


    if ball.distance(paddle) < 50 and ball.xcor() > 320:
        ball.bounce2()
        ball.speedup()
    elif ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce2()
        ball.speedup()


    if ball.xcor() > 380:
        ball.reposition()
        score.Score1()
    elif ball.xcor() < -380:
        ball.reposition()
        score.Score2()

screen.exitonclick()
