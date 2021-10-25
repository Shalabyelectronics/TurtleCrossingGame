import turtle
import random


# COLORS = pass

class Car(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.position = []
        self.generate_position()
        self.segments = []
        self.car_colors = ['yellow', 'gold', 'orange', 'red', 'violet',
                           'magenta', 'purple', 'navy', 'blue', 'maroon', 'cyan', 'turquoise', 'green', 'chocolate', 'brown', 'black', 'gray']
        self.pick_color = random.choice(self.car_colors)
        self.create_car_segments(color=self.pick_color)
        self.car_position = self.segments[0]

    def generate_position(self):
        y_position = random.randint(-230, 250)
        x_position = random.randint(500, 2000)
        for pos in range(3):
            self.position.append((x_position, y_position))
            y_position -= 20

    def create_car_segments(self, color):
        for pos in range(len(self.position)):
            car_seg = turtle.Turtle()
            car_seg.shape("square")
            car_seg.penup()
            car_seg.goto(self.position[pos])
            self.segments.append(car_seg)
        for seg in self.segments:
            seg.color(color)

    def move_car(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].setheading(180)
        self.segments[0].forward(20)
