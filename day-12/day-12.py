from art import logo
import random
import os

EASY_LIVES = 10
HARD_LIVES = 5

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def random_number():
    number = random.randint(1, 100)
    return number

def game_lvl():
    """Choose a difficulty level."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LIVES
    elif level == "hard":
        return HARD_LIVES
    else:
        print("Invalid input. Please try again.")
        game_lvl()

def play_again():
    """Play again or not?"""
    again = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if again == "y":
        os.system("cls")
        print(logo)
        guess()
    elif again == "n":
        print("Goodbye.")
    else:
        print("Invalid input. Please try again.")
        play_again()

def guess():
    number = random_number()
    lives = game_lvl()
    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        #print(f"Number: {number}")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}.")
            return
        elif guess > number:
            print("Too high.")
            lives -= 1
        elif guess < number:
            print("Too low.")
            lives -= 1
    print("You've run out of guesses, you lose.")

if __name__ == "__main__":
    guess()
    play_again()
