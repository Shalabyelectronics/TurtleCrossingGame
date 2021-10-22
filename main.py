from turtle import Screen
from player import Player
from levels import Levels

screen = Screen()
screen.setup(1000, 600)
screen.title("Turtle Crossing Game")
player = Player()
levels = Levels()

screen.listen()
screen.onkey(key="Up", fun=player.move_up)
screen.exitonclick()
