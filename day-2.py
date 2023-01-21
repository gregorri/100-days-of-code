#print("hello"[4])

#num_char = len(input("What is your name? "))
#new_num_char = str(num_char)
#print("Your name has " + new_num_char + " characters.")

#two_dgit_number = input("Type a two digit number: ")
#first_digit = int(two_dgit_number[0])
#second_digit = int(two_dgit_number[1])
#print(first_digit + second_digit)

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(weight) / float(height) ** 2

print(int(bmi))