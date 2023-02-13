# from turtle import Turtle, Screen
#
# timy = Turtle()
# screen = Screen()
# timy.shape("turtle")
# timy.color("red")
#
# print(screen.candlelight)
# screen.exitonclick()
from prettytable import PrettyTable
from prettytable import from_csv

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)
