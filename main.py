from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Camy's Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.face.distance(food) < 10:
        food.refresh()
        snake.extend()
        score.gain_point()
        score.update_scoreboard()
    if snake.face.xcor() > 280 or snake.face.xcor() < -280 or snake.face.ycor() > 280 or snake.face.ycor() < -280:
        score.reset()
        score.update_scoreboard()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.face.distance(segment) < 10:
            score.reset()
            score.update_scoreboard()
            snake.reset()

screen.exitonclick()
