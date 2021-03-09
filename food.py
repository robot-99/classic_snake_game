from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-260, 260, 20)
        self.goto(x, y)
