from turtle import Turtle


class Levels(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.goto(-400, 260)
        self.level_update()
        self.speed_cars = 0.2

    def level_update(self):
        self.clear()
        self.write(f"Level : {self.level}", align="center", font=("Courier", 25, "normal"))

    def increase_level(self):
        self.level += 1

    def increase_speed(self):
        self.speed_cars *= 0.8

    def game_over(self):
        self.goto(-50, 200)
        self.write("Game Over", align="center", font=("Courier", 50, "bold"))

