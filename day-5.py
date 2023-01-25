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


total = 0   
for number in range(1, 101):
    total += number
print(total)