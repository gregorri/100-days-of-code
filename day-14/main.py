from data_format import FormatData, CheckAnswer
from art import logo, vs
from info import data
import random
from replit import clear


def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_b = random.choice(data)

    while game_should_continue:
        account_a = account_b  # Make account at position B become the next account at position A.
        account_b = random.choice(data)  #

        if account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {FormatData(account_a).format_data()}.")
        print(vs)
        print(f"Against B: {FormatData(account_b).format_data()}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = CheckAnswer(guess, a_follower_count, b_follower_count).check_answer()

        clear()
        print(logo)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}.")


game()
