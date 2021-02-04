from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # the background of the canvas
screen.title("My Snake Game")
screen.tracer(0)  # so the screen does not update until we do: screen.update

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Making the snake move
game_is_on = True

while game_is_on:
    screen.update()  # to update the screen
    time.sleep(0.1)  # 0.1s delay
    snake.move()

screen.exitonclick()
