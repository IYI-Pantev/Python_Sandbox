import random
import turtle as t # alias for turtle

tim = t.Turtle()
tim.shape("turtle")
# tim.color("maroon", "yellow green")

#square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

#dashed line
# for i in range(15):
#
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


"""from triangle to decagon"""
import data

for i in range(len(data.rainbow_colours)):
    tim.color(data.rainbow_colours[i])
    sides = i + 3
    for _ in range(sides):
        tim.right(360/sides)
        tim.forward(100)

# """random walk"""
#
#
# def random_colour():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
# print(random_colour())
# 
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(100):
#     tim.color()
#     tim.forward(30)
#     tim.setheading(random.choice(directions))



screen = t.Screen()
screen.exitonclick()