
from turtle import Turtle
import random

COLORS = ["blue", "red", "yellow", "purple"]
SHAPE = "turtle"

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.set_random_color()
        self.speed("fastest")
        self.refresh()

    def set_random_color(self):
        color = random.choice(COLORS)
        self.color(color)

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.set_random_color()
        self.goto(random_x, random_y)