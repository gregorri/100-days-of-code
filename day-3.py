# """ 
# number = int(input("Which number do you want to check? "))

# if number % 2 == 0:
#     print("This number is even")
# else:
#     print("This number is add") 
# """


# """ print("Welcome to the rollercoaster!")
# height = int(input("What is your height i cm?"))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7")
#     elif age >= 45 and age <= 55:
#         print("Everything is going to be ok. Have a free ride on us!")
#     else:
#         bill = 12
#         print("Adult tickets are $12") 

#     wants_photo = input("Do you want a photo taken? Y or N. ") 
#     if wants_photo == "Y":
#         bill += 3
#         print("Your photo will cost $3") 
    
#     print(f"Your final bill is ${bill}")
# else:
#     print("Sorry, you have to grow taller before you can ride.")  """


# """ 
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# bmi = round(weight / height ** 2)
# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.") 
# """

# """ 
# year = int(input("Which year do you want to check? "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.") 
# """

# """ 
# print("Welcome to Pizza Deliveries!")

# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your bill is ${bill}") """

# """ print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# combined_string = name1 + name2
# lover_case_string = combined_string.lower()

# t = lover_case_string.count("t")
# r = lover_case_string.count("r")
# u = lover_case_string.count("u")
# e = lover_case_string.count("e")
# l = lover_case_string.count("l")
# o = lover_case_string.count("o")
# v = lover_case_string.count("v")
# e = lover_case_string.count("e")

# true = t + r + u + e
# love = l + o + v + e

# count = int(str(true) + str(love))
# if count < 10 or count > 90:
#     print(f"Your score is {count}, you go together like coke and mentos.")
# elif count >= 40 and count <= 50:
#     print(f"Your score is {count}, you are alright together.")
# else:
#     print(f"Your score is {count}.") """

# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
# direction = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' \n").lower()

# if direction == "left":
#     action = input("You\'ve come to a Lake. There is an island in the middle of the Lake.Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
#     if action == "wait":
#         door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
#         if door == "red":
#             print("It's a room full of fire. Game Over.")
#         elif door == "yellow":
#             print("You found the treasure! You Win!")
#         elif door == "blue":
#             print("You enter a room of beasts. Game Over.")
#         else:
#             print("You chose a door that doesn't exist. Game Over.")
#     else:
#         print("You get attacked by an angry trout. Game Over.")
# else:
#     print("You fell into a hole. Game Over.")
