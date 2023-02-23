from turtle import Turtle


class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.high_score = 0
		self.color("white")
		self.penup()
		self.hideturtle()
		self.goto(0, 270)
		self.update_scoreboard()

	def update_scoreboard(self):
		self.write(f"Score: {self.score}    Higher Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

	def game_over(self):
		self.goto(0, 0)
		self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

	def increase_score(self):
		self.score += 1
		self.high_score = max(self.score, self.high_score)
		self.clear()
		self.update_scoreboard()
