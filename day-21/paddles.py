from turtle import Turtle


class Paddle(Turtle):
	def __init__(self, position):
		super().__init__()
		self.shape("square")
		self.color("white")
		self.shapesize(stretch_wid=5, stretch_len=1)
		self.penup()
		self.goto(position)

	def right_paddle(self):
		self.goto(380, 0)

	def go_up(self):
		new_y = self.ycor() + 20
		self.goto(self.xcor(), new_y)

	def go_down(self):
		new_y = self.ycor() - 20
		self.sety(new_y)
		self.goto(self.xcor(), new_y)

	def move_the_paddle(self):
		self.go_up()
		self.go_down()

	def reset_position(self):
		self.goto(-380, 0)
