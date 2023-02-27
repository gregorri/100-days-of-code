from turtle import Screen
from ball import Ball
from paddles import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((380, 0))
left_paddle = Paddle((-380, 0))
ball = Ball()
#scoreboard = Scoreboard()

screen.listen()
screen.onkey(Paddle.go_up, "Up")
screen.onkey(Paddle.go_down, "Down")

game_is_on = True
while game_is_on:
	screen.update()
	time.sleep(ball.move_speed)
	ball.move()

	# Move the paddle
	Paddle.move_the_paddle(self=right_paddle)

	# Detect collision with wall
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_y()
	# # Detect collision with paddle
	# if ball.distance(Paddle) < 50 and ball.xcor() > 340 or ball.distance(Paddle) < 50 and ball.xcor() < -340:
	# 	ball.bounce_x()
	# # Detect when paddle misses
	# if ball.xcor() > 380 or ball.xcor() < -380:
	# 	ball.reset_position()
	# 	#scoreboard.increase_score()






screen.exitonclick()