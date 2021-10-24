from turtle import Screen
from player import Player
from levels import Levels
from car import Car
import time

screen = Screen()
screen.setup(1000, 600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
player = Player()
levels = Levels()
cars = []

for _ in range(20):
    car = Car()
    cars.append(car)

screen.listen()
screen.onkey(key="Up", fun=player.move_up)

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    for car in cars:
        car.move_car()
    if player.ycor() > 250:
        levels.increase_level()
        levels.level_update()
        player.reset_player()


screen.exitonclick()
