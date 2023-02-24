from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Create window screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


# Listen for key-presses to move the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
	screen.update()     # update screen
	time.sleep(0.1)     # delay
	snake.move()

	# Detect collision with food
	if snake.head.distance(food) < 15:  # 15 is the distance between the snake head and the food
		scoreboard.increase_score()
		snake.extend()
		food.refresh()


screen.exitonclick()
