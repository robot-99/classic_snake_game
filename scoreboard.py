from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("score.txt", mode="r") as score:
            high_score = score.read()
        self.high_score = int(high_score)
        self.penup()
        self.setposition(0, 270)
        self.score = 0
        self.color("white")
        self.write(f"Your score is: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def gain_point(self):
        self.clear()
        self.score += 1

    def update_scoreboard(self):
        self.clear()
        self.write(f"Your score is: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open("score.txt", mode="w") as file:
            file.write(f"{self.high_score}")
