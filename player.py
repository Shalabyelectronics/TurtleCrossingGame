from turtle import Turtle


class Player(Turtle):
    def __init__(self, x_pos, color):
        super().__init__()
        self.shape("turtle")
        self.shapesize(1)
        self.color(color)
        self.setheading(90)
        self.penup()
        self.rest_pos = x_pos
        self.goto(x_pos, -280)

    def move_up(self):
        self.forward(10)

    def reset_player(self):
        self.goto(self.rest_pos, -280)

