import turtle as t
import random

tim = t.Turtle()

def random_color():
	r = random.random()
	g = random.random()
	b = random.random()
	color = (r, g, b)
	return color


def draw_shape(num_sides):
	angle = 360 / num_sides
	tim.color(random_color())
	for _ in range(num_sides):
		tim.forward(100)
		tim.right(angle)

def draw_spirograph(size_of_gap):
	for _ in range(int(360 / size_of_gap)):
		tim.color(random_color())
		tim.circle(100)
		tim.setheading(tim.heading() + size_of_gap)

for shape_side_n in range(3, 11):
	draw_shape(shape_side_n)

