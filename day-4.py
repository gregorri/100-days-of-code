""" import random

random_integer = random.randint(1, 10)
print(random_integer) """

""" import random

tell_the_user = random.randint(0, 1)
if tell_the_user == 0:
    print("Heads")
else:
    print("Tails")
print(tell_the_user) """

""" import random

flip = random.choice(["Heads", "Tails"])
print(flip) """

""" states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", 
"North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", 
"Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", 
"Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(len(states_of_america)) """

""" import random
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
name_string = random.choice(names)
print(name_string) """
# import random

# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# random_names = random.choice(names)

# print(f"{random_names} is going to buy the meal today!")

""" row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical -1]
selected_row[horizontal -1] = "X"

print(f"{row1}\n{row2}\n{row3}")
 """
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

store_choice = [rock, paper, scissors]
bot = random.choice(store_choice)
user = store_choice[choice]

print(f"You chose: {user}")
print(f"Computer chose: {bot}")

if user == bot:
    print("It's a draw")
elif user == rock and bot == paper:
    print("You lose")
elif user == rock and bot == scissors:
    print("You win")
elif user == paper and bot == rock:
    print("You win")
elif user == paper and bot == scissors:
    print("You lose")
elif user == scissors and bot == rock:
    print("You lose")
elif user == scissors and bot == paper:
    print("You win")
else:
    print("Invalid input")


