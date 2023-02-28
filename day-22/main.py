import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

# Move the player up when the "Up" key is pressed
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_up, "w")
screen.onkey(player.use_power, "space")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()




screen.exitonclick()
