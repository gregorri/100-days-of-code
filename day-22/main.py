import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Move the player up when the "Up" key is pressed
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_up, "w")
screen.onkey(player.use_power, "space")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Add cars to the screen
    car_manager.create_car()
    # Move the cars
    car_manager.move_cars()
    # Add score board
    scoreboard.update_scoreboard()

    # Add 1 to the score when the player reaches the finish line
    if player.finish_line():
        player.reset()
        car_manager.level_up()
        scoreboard.increase_score()


    # Detect collision with the cars
    for car in car_manager.all_cars:
        if car.distance(player.player) < 20:
            game_is_on = False
            scoreboard.game_over()




screen.exitonclick()
