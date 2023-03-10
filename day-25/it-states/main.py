import pandas
import turtle

screen = turtle.Screen()
screen.title("Italian States")
image = "R.gif"
screen.addshape(image)
turtle.shape(image)



# def get_mouse_click_coor(x, y):
# 	print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

# Rea the csv file
data = pandas.read_csv("it_states.csv")
all_states = data.Capoluogo.to_list()
guessed_states = []

while len(guessed_states) < 20:
	answer_state = screen.textinput(title=f"{len(guessed_states)}/20 States Correct", prompt="What's another state's name?").title()

	if answer_state == "Exit":
		missing_states = [state for state in all_states if state not in guessed_states] # list comprehension
		new_data = pandas.DataFrame(missing_states)
		new_data.to_csv("states_to_learn.csv")
		break
	if answer_state in all_states:
		guessed_states.append(answer_state)
		t = turtle.Turtle()
		t.hideturtle()
		# t.write(answer_state, font=("Arial", 8, "bold"))
		t.penup()
		state_data = data[data.Capoluogo == answer_state]
		t.goto(int(state_data.x), int(state_data.y))
		t.write(answer_state)
