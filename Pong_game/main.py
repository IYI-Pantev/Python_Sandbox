from turtle import Screen
from padle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

RIGHT_PAD_COORDINATES = (350, 0)
LEFT_PAD_COORDINATES = (-350, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_pad = Paddle(RIGHT_PAD_COORDINATES)
left_pad = Paddle(LEFT_PAD_COORDINATES)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(right_pad.go_up, "Up")
screen.onkey(right_pad.go_down, "Down")

screen.onkey(left_pad.go_up, "w")
screen.onkey(left_pad.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with r_paddle
    if ball.distance(right_pad) < 50 and ball.xcor() > 320 or ball.distance(left_pad) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when  R pad misses
    if ball.xcor() > 360:
        ball.reset_position()
        score.l_point()

    # # detect when  L pad misses
    if ball.xcor() < -360:
        ball.reset_position()
        score.r_point()


screen.exitonclick()
