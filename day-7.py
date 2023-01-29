import random
import string

word = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word)
word_length = len(chosen_word)

print(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

guess = input("Guess a letter: ").lower()


guessed_letters = False
while not guessed_letters:
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if guess == "quit":
        break
    if "_" not in display:
        guessed_letters = True
        print("You win.")
    else:
        guess = input("Guess a letter: ").lower()
        

print(display)