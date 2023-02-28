from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
MOVE_DISTANCE_INCREASE = 50
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        self.player = Turtle()
        self.player.shape("turtle")
        self.player.penup()
        self.player.setheading(90)
        self.player.goto(STARTING_POSITION)

    def go_up(self):
        self.player.forward(MOVE_DISTANCE)

    def reset(self):
        self.player.goto(STARTING_POSITION)

    def finish_line(self):
        if self.player.ycor() > FINISH_LINE_Y:
            return True

    def use_power(self):
        self.player.forward(MOVE_DISTANCE_INCREASE)
