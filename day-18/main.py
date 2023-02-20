# import turtle as t
# import random
#
# tim = t.Turtle()
# screen = t.Screen()
# t.colormode(255)
# tim.speed("fastest")
#
#
# def random_color():
# 	r = random.randint(0, 255)
# 	g = random.randint(0, 255)
# 	b = random.randint(0, 255)
# 	color = (r, g, b)
# 	return color
#
#
# def draw_spirograph(size_of_gap):
# 	for _ in range(int(360 / size_of_gap)):
# 		tim.color(random_color())
# 		tim.circle(100)
# 		tim.setheading(tim.heading() + size_of_gap)
#
#
# draw_spirograph(5)
#
# t.exitonclick()

# import colorgram
#
# colors = colorgram.extract('image.jpg', 20)
# rgb_colors = []
# for color in colors:
# 	r = color.rgb.r
# 	g = color.rgb.g
# 	b = color.rgb.b
# 	new_color = (r, g, b)
# 	rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
import random

color_list = [(229, 228, 227), (226, 224, 225), (198, 175, 119), (125, 36, 23), (187, 157, 50), (170, 104, 56), (5, 56, 83), (201, 216, 205), (109, 67, 85), (39, 35, 34),
              (223, 224, 227), (84, 141, 61), (20, 122, 175), (111, 161, 176), (75, 38, 48), (8, 67, 47), (65, 154, 134), (132, 41, 43), (184, 98, 81), (183, 180, 181)]
tim = t.Turtle()
tim.hideturtle()
screen = t.Screen()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.goto(-250, -250)


def draw_dots():
	for _ in range(10):
		tim.dot(20, random.choice(color_list))
		tim.penup()
		tim.forward(50)


def draw_square():
	for _ in range(10):
		draw_dots()
		tim.setheading(90)
		tim.forward(50)
		tim.setheading(180)
		tim.forward(500)
		tim.setheading(0)


draw_square()
t.exitonclick()
