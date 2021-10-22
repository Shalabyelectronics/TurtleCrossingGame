from turtle import Screen
from player import Player

screen = Screen()
screen.setup(1000, 600)
screen.title("Turtle Crossing Game")
player = Player()
screen.listen()
screen.onkey(key="Up", fun=player.move_up)
screen.exitonclick()
