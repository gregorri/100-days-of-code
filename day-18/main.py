import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)
tim.pensize(2)
tim.speed("fastest")


def random_color():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	color = (r, g, b)
	return color

for i in range(40):
	tim.color(random_color())
	tim.circle(100)
	tim.left(10)

t.exitonclick()