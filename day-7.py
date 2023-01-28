import random
import string

word = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word)
print(chosen_word)

display = []
word_length = len(chosen_word)
for letter in range(word_length):
    display += "_"
guess = input("Guess a letter: ").lower()


for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)