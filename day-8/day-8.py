# import random
# import math

# def paint_calc(height, width, cover):
#     number_of_cans = math.ceil((height * width) / cover)
#     print(f"You'll need {number_of_cans} cans of paint.")

# test_h = int(input("Height of wall: "))#random.randint(1, 100)
# test_w = int(input("Width of wall: "))#random.randint(1, 100)
# coverage = 5

# print(f"Height: {test_h}")
# print(f"Width: {test_w}")
# paint_calc(height=test_h, width=test_w, cover=coverage)

# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")


# n = int(input("Check this number: "))
# prime_checker(number=n)
# from art import logo

# alphabet = "abcdefghijklmnopqrstuvwxyz"

# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = ""
#     if cipher_direction == "decode":
#         shift_amount *= -1
#     for char in start_text:
#         if char in alphabet:
#             position = alphabet.index(char)
#             new_position = (position + shift_amount) % len(alphabet)
#             end_text += alphabet[new_position]
#         else:
#             end_text += char
#     print(f"The {cipher_direction}d text is {end_text}")

# print(logo)
# #figure out a way to ask the user if they want to restart the cipher program
# while True:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
#     text = input("Type your message: ").lower()
#     shift = int(input("Type the shift number: "))
#     caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
#     restart = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")
#     if restart == "no":
#         print("Goodbye")
#         break

