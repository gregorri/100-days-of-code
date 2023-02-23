from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
	def __init__(self):
		self.all_segments = []
		self.create_snake()

	def create_snake(self):
		"""Create the snake body"""
		for position in STARTING_POSITIONS:
			new_segment = Turtle("square")
			new_segment.color("white")
			new_segment.penup()
			new_segment.goto(position)
			self.all_segments.append(new_segment)

	def move(self):
		"""Move the snake forward by 20 pixels"""
		for seg_num in range(len(self.all_segments) - 1, 0, -1):
			new_x = self.all_segments[seg_num - 1].xcor()
			new_y = self.all_segments[seg_num - 1].ycor()
			self.all_segments[seg_num].goto(new_x, new_y)
		self.all_segments[0].forward(20)

	def up(self):
		"""Move the snake up by 20 pixels"""
		self.all_segments[0].setheading(90)

	def down(self):
		"""Move the snake down by 20 pyxels"""
		self.all_segments[0].setheading(270)

	def left(self):
		self.all_segments[0].setheading(180)

	def right(self):
		self.all_segments[0].setheading(0)
