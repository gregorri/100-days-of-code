""" fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
    print(fruit + ' pie') """

""" student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# Method 1
# toral_height = sum(student_heights)
# number_of_students = len(student_heights)
# average_height = round(toral_height / number_of_students)
# print(average_height)

# Method 2
total_height = 0
for height in student_heights:
    total_height += height
#print(total_height)

number_of_students = 0
for student in student_heights:
    number_of_students += 1
#print(number_of_students)

average_height = round(total_height / number_of_students)
print(f"The average height is {average_height} cm") """

""" student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max_score = student_scores[0]

for score in student_scores:
    if score > max_score:
        max_score = score

print(f"The highest score in the class is: {max_score}") """


""" total = 0   
for number in range(1, 101):
    if number % 2 == 0:
        #print(number)
        total += number
print(total) """

""" for number in range(1, 100):
    if number % 3 == 0 and number % 5 == 0 :
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number) """

# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))


# # random_letters = random.choices(letters, k=nr_letters)
# # random_symbols = random.choices(symbols, k=nr_symbols)
# # random_numbers = random.choices(numbers, k=nr_numbers)
# # password = random_letters + random_symbols + random_numbers
# # random.shuffle(password)
# # password = "".join(password)
# # print(f"Your password is: {password}")
# password = ""
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
# password_list = list(password)
# random.shuffle(password_list)
# password = "".join(password_list)
# print(f"Your password is: {password}")