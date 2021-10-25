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
player = Player(x_pos=50, color="black")
asma = Player(x_pos=-50, color="blue")
levels = Levels()
cars = []

screen.listen()
screen.onkey(key="Up", fun=player.move_up)
screen.onkey(key="w", fun=asma.move_up)

game_on = True
for _ in range(15):
    car = Car()
    cars.append(car)
while game_on:
    time.sleep(levels.speed_cars)
    screen.update()
    for car in cars:
        car.move_car()
        for car_seg in car.segments:
            if car_seg.xcor() < -500:
                y_position = random.randint(-230, 250)
                x_position = random.randint(500, 2000)
                car.segments[0].goto(x_position, y_position)
            if player.distance(car_seg) < 8 or asma.distance(car_seg) < 8:
                levels.game_over()
                game_on = False
    if player.ycor() > 250:
        levels.increase_level()
        levels.level_update()
        player.reset_player()
        asma.reset_player()
        levels.increase_speed()
    if asma.ycor() > 250:
        levels.increase_level()
        levels.level_update()
        asma.reset_player()
        levels.increase_speed()



screen.exitonclick()
