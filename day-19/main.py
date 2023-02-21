from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=700, height=400)
user_input = screen.textinput(title="Make your bet", prompt="Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

is_race_on = False

for turtle_index in range(6):
	tim = Turtle(shape="turtle")
	tim.color(color[turtle_index])
	tim.penup()
	tim.goto(-330, y_positions[turtle_index])
	all_turtles.append(tim)

if user_input:
	is_race_on = True

while is_race_on:
	for turtle in all_turtles:
		if turtle.xcor() > 230:
			is_race_on = False
			winning_color = turtle.pencolor()
			if winning_color == user_input:
				print(f"You've won! The {winning_color} turtle is the winner!")
			else:
				print(f"You've lost! The {winning_color} turtle is the winner!")

		random_distance = random.randint(0, 10)
		turtle.forward(random_distance)

screen.exitonclick()
