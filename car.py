import turtle
import random


class Car(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.position = []
        self.generate_position()
        self.segments = []
        self.create_car()
        self.car_position = self.segments[0]

    def generate_position(self):
        y_position = random.randint(-230, 250)
        x_position = random.randint(500, 600)
        for pos in range(3):
            self.position.append((x_position, y_position))
            y_position -= 20

    def create_car(self):
        for pos in range(len(self.position)):
            car_seg = turtle.Turtle()
            car_seg.shape("square")
            car_seg.penup()
            self.color("black")
            car_seg.goto(self.position[pos])
            self.segments.append(car_seg)

    def move_car(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].setheading(180)
        self.segments[0].forward(20)
