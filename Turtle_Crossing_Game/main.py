import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

turtle = Player()
score = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(fun=turtle.move, key="w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(turtle) < 25:
            game_is_on = False
            score.game_end()

    if turtle.ycor() > 230:
        score.update_score()
        turtle.start_position()
        car_manager.speed_up()

screen.exitonclick()
