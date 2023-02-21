from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet", prompt="Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "black", "white", "grey"]
y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(6):
	tim = Turtle(shape="turtle")
	tim.color(color[turtle_index])
	tim.penup()
	tim.goto(-230, y_positions[turtle_index])

screen.exitonclick()
