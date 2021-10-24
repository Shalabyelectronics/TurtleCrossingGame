from turtle import Screen
from player import Player
from levels import Levels
import random
from car import Car
import time

screen = Screen()
screen.setup(1000, 600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
player = Player()
levels = Levels()
cars = []



screen.listen()
screen.onkey(key="Up", fun=player.move_up)

game_on = True
for _ in range(10):
    car = Car()
    cars.append(car)
while game_on:
    time.sleep(0.1)
    screen.update()
    for car in cars:
        car.move_car()
        for car_seg in car.segments:
            if car_seg.xcor() < -500:
                y_position = random.randint(-230, 250)
                x_position = random.randint(500, 2000)
                car.segments[0].goto(x_position, y_position)
            if player.distance(car_seg) < 17:
                game_on = False
    if player.ycor() > 250:
        levels.increase_level()
        levels.level_update()
        player.reset_player()

screen.exitonclick()
