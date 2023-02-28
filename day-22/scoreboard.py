from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def reset(self):
        self.score = 0
        self.clear()
        self.update_scoreboard()

