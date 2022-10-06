from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# Up Arrow
def move_forward():
    tim.forward(10)

screen.listen()
screen.onkey(key="w", fun=move_forward) # act as Higher Order Function

# Down Arrow
def move_backward():
    tim.backward(10)

screen.onkey(key="s", fun=move_backward)

# Left Arrow
def move_left():
    tim.left(10)

screen.onkey(key="a", fun=move_left)

# Right Arrow
def move_right():
    tim.right(10)

screen.onkey(key="d", fun=move_right)

def clear_drawing():
    tim.reset()

screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()