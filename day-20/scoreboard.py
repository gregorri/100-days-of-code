from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Calibri", 24, "normal")


class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.reset_button = Turtle()
		self.score = 0
		self.high_score = 0
		self.color("white")
		self.penup()
		self.hideturtle()
		self.goto(0, 270)
		self.update_scoreboard()

	def update_scoreboard(self):
		self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

	def increase_score(self):
		self.score += 1
		self.high_score = max(self.score, self.high_score)
		self.clear()
		self.update_scoreboard()

	def game_over(self):
		self.goto(0, 0)
		self.clear()
		self.write(f"Game Over\n    Score: {self.score}", align=ALIGNMENT, font=("Calibri", 40, "bold"))
		self.hideturtle()
		# self.add_reset_button()




