from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 28, "normal")
WELCOME_FONT = ("Courier", 34, "normal")
COLOR = "black"

class Welcome(Turtle):

    def __init__(self):
        super().__init__()
        self.text = "Welcome to RG-Snake Game"
        self.color(COLOR)
        self.penup()
        self.goto(0, 270)
        self.set_welcome_text()
        self.want_to_play()
        self.hideturtle()

    def set_welcome_text(self):
        self.goto(0, 140)
        self.write(f"{self.text}", align=ALIGNMENT, font=WELCOME_FONT)

    # def increase_score(self):
    #     self.score += 1
    #     self.clear()
    #     self.update_scoreboard()

    def want_to_play(self):
        self.goto(0, 0)
        self.write(f"Press 'g' to Play!!", align=ALIGNMENT, font=FONT)

