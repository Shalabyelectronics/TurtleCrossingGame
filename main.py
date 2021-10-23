from turtle import Screen
from player import Player
from levels import Levels
import time

screen = Screen()
screen.setup(1000, 600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
player = Player()
levels = Levels()

screen.listen()
screen.onkey(key="Up", fun=player.move_up)

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() > 250:
        levels.increase_level()
        levels.level_update()


screen.exitonclick()
