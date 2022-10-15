from turtle import Turtle

X_POSITION = 0
Y_POSITION = 270
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highest_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(X_POSITION, Y_POSITION)
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def score_refresh(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score} Highest score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highest_score}")
        self.score = -1
        self.score_refresh()
