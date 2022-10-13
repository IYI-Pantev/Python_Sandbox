from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.level = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.level += 1
        self.goto(-210, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_end(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=FONT)
