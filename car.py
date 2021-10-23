import turtle
import random

POSITION = [(0, 0), (20, 0), (40, 0)]


class Car(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        turtle.colormode(255)
        self.segments = []
        self.create_car()
        self.car_position = self.segments[0]
        self.car_position.goto(440, 0)
        self.car_position.setheading(180)


    def create_car(self):
        for pos in range(len(POSITION)):
            color = random.randint(0, 255)
            car = turtle.Turtle()
            car.shape("square")
            car.penup()
            car.color((color, color, color))
            car.goto(POSITION[pos])
            self.segments.append(car)

    def move_car(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(20)
