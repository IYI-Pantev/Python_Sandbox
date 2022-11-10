import turtle as t
import random
from data import rainbow_colours

tim = t.Turtle()
tim.shape("turtle")

tim.color("red", "green")
tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random.choice(rainbow_colours))
        tim.circle(-100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
