from turtle import Turtle


class Scoreboard(Turtle):
	def __init__(self , position):
		super().__init__()
		self.color("white")
		self.penup()
		self.hideturtle()
		self.score = 0
		self.goto(position)
		self.update_scoreboard()

	def update_scoreboard(self):
		self.clear()

		self.write(self.score, align="center", font=("Courier", 50, "bold"))

	def increase_score(self):
		self.score += 1
		self.update_scoreboard()

	def game_over(self):
		self.goto(0, 0)
		self.write("GAME OVER", align="center", font=("Courier", 50, "bold"))
		# Print the final score and the player who won
		if self.score == 5:
			self.goto(0, -50)
			self.write("Player 1 wins", align="center", font=("Courier", 50, "bold"))
		else:
			self.goto(0, -50)
			self.write("Player 2 wins", align="center", font=("Courier", 50, "bold"))
