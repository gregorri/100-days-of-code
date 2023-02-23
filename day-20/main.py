from turtle import Turtle, Screen
from snake import Snake
import time

# Create window screen
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
	screen.update() # update screen
	time.sleep(0.4) # delay

	snake.move()


screen.exitonclick()