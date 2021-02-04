from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # the background of the canvas
screen.title("My Snake Game")
screen.tracer(0)  # so the screen does not update until we do: screen.update

snake = Snake()

# Making the snake move
game_is_on = True

while game_is_on:
    screen.update()  # to update the screen
    time.sleep(0.1)  # 0.1s delay

    snake.move()

screen.exitonclick()
