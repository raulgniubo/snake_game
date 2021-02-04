from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # the background of the canvas
screen.bgpic("bg.gif")
screen.title("My Snake Game")
screen.tracer(0)  # so the screen does not update until we do: screen.update

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detecting collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # detecting collision with tail
    # if head collides with any segment in the tail:
        # trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
