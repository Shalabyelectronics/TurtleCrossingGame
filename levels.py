from turtle import Turtle


class Levels(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.goto(-400, 260)
        self.level_update()

    def level_update(self):
        self.clear()
        self.write(f"Level : {self.level}", align="center", font=("Courier", 25, "normal"))

    def increase_level(self):
        self.level += 1
