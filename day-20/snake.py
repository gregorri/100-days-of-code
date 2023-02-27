from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 17
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
	def __init__(self):
		self.all_segments = []
		self.create_snake()
		self.head = self.all_segments[0]

	def create_snake(self):
		"""Create the snake body"""
		for position in STARTING_POSITIONS:
			self.add_segment(position)

	def move(self):
		"""Move the snake forward by 20 pixels"""
		for seg_num in range(len(self.all_segments) - 1, 0, -1):
			new_x = self.all_segments[seg_num - 1].xcor()
			new_y = self.all_segments[seg_num - 1].ycor()
			self.all_segments[seg_num].goto(new_x, new_y)
		self.head.forward(MOVE_DISTANCE)

	def add_segment(self, position):
		"""Add a new segment to the snake"""
		new_segment = Turtle("square")
		new_segment.color("white")
		new_segment.penup()
		new_segment.goto(position)
		self.all_segments.append(new_segment)

	def extend(self):
		"""Add a new segment to the snake"""
		self.add_segment(self.all_segments[-1].position())

	def up(self):
		"""Move the snake up by 20 pixels"""
		if self.head.heading() != DOWN:
			self.head.setheading(UP)

	def down(self):
		"""Move the snake down by 20 pyxels"""
		if self.head.heading() != UP:
			self.head.setheading(DOWN)

	def left(self):
		if self.head.heading() != RIGHT:
			self.head.setheading(LEFT)

	def right(self):
		if self.head.heading() != LEFT:
			self.head.setheading(RIGHT)


