from question_model import Question
from data import question_data

question_bank = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

print(question_bank)
