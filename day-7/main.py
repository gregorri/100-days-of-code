import random
import string
from hangman_art import stages, logo
from hangman_words import word_list

def print_display(display):
    print(f"{' '.join(display)}")

def check_guess(guess, display, chosen_word):
    if guess in display:
        print(f"You've already guessed {guess}")
        return False

    guessed = False
    word_length = len(chosen_word)
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            guessed = True
    if not guessed:
        print(f"You guessed {guess}, that's not in the word.")
        return False
    return True

def play_hangman():
    print(logo)
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    guessed_letters = False
    lives = 6
    display = ["_" for _ in range(word_length)]

    print(f"pssst, the solution is {chosen_word}.")

    while not guessed_letters:
        guess = input("Guess a letter: ").lower()
        if guess == "quit":
            break
        if check_guess(guess, display, chosen_word):
            print_display(display)
            if "_" not in display:
                guessed_letters = True
                print("You win.")
                break
        else:
            lives -= 1
            if lives == 0:
                guessed_letters = True
                print("You lose.")
                break
        print(stages[lives])

play_hangman()

