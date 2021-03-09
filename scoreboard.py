from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(0, 270)
        self.score = 0
        self.write(f"Your score is: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def gain_point(self):
        self.clear()
        self.score += 1
        self.write(f"Your score is: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

