import turtle
import random


class Car(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        turtle.colormode(255)
        self.position = []
        self.generate_position()
        self.segments = []
        self.create_car()
        self.car_position = self.segments[0]

    def generate_position(self):
        y_position = random.randint(-250, 250)
        for pos in range(3):
            self.position.append((500, y_position))
            y_position -= 20

    def create_car(self):
        for pos in range(len(self.position)):
            color = random.randint(0, 255)
            car = turtle.Turtle()
            car.shape("square")
            car.penup()
            car.color((color, color, color))
            car.goto(self.position[pos])
            self.segments.append(car)

    def move_car(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].setheading(180)
        self.segments[0].forward(20)
