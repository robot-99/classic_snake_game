from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.face = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.color("blue")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.reset()
        self.segments.clear()
        self.create_snake()
        self.face = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.face.forward(MOVE_DISTANCE)

    def up(self):
        if not self.face.heading() == DOWN:
            self.face.setheading(UP)

    def down(self):
        if not self.face.heading() == UP:
            self.face.setheading(DOWN)

    def left(self, **kwargs):
        if not self.face.heading() == RIGHT:
            self.face.setheading(LEFT)

    def right(self, **kwargs):
        if not self.face.heading() == LEFT:
            self.face.setheading(RIGHT)
