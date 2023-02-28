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
right_scoreboard = Scoreboard((100, 200))
left_scoreboard = Scoreboard((-100, 200))

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
	screen.update()
	time.sleep(0.1)
	ball.move()
	# Detect collision with wall
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_y()
	# Detect collision with paddle
	if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
		ball.bounce_x()
	# Detect when paddle misses
	if ball.xcor() > 380:
		ball.reset_position()
		left_scoreboard.increase_score()
	if ball.xcor() < -380:
		ball.reset_position()
		right_scoreboard.increase_score()
	# Game over print the winner
	if left_scoreboard.score == 5 or right_scoreboard.score == 5:
		game_is_on = False
		right_scoreboard.game_over()
		left_scoreboard.game_over()






screen.exitonclick()