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

car = Car()




screen.listen()
screen.onkey(key="Up", fun=player.move_up)


game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    car.move_car()
    for car_seg in car.segments:
        if car_seg.xcor() < -500:
            car.segments[0].goto(500, 0)
    if player.ycor() > 250:
        levels.increase_level()
        levels.level_update()
        player.reset_player()

screen.exitonclick()
