print("Hide the credit card number")

def hide_credit_card_number(credit_card_number):
    last_four = credit_card_number[-4:]
    hidden = "*" * (len(credit_card_number) - 4)
    return hidden + last_four

credit_card_number = input("Enter a credit card number: ")
print(hide_credit_card_number(credit_card_number))