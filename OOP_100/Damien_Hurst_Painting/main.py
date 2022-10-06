import colorgram
import turtle as t
import random

# rgb_colors = []
# colors = colorgram.extract('hirst_dots.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


color_list = [(238, 246, 243), (246, 240, 244), (235, 241, 246), (1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58), (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85), (145, 227, 216), (122, 193, 148), (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179)]

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255) # ! to be able to use rgb colors

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)

tim.hideturtle()
for _ in range(5):
    # print dots
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

    # left turn
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(50)

    # print dots
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

    # right turn
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(0)
    tim.forward(50)


screen = t.Screen()
screen.exitonclick()
