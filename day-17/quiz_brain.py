class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.user_answer = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Get the next question from the list and check if the answer is correct."""
        current_question = None
        if self.question_number < len(self.question_list):
            current_question = self.question_list[self.question_number]
        else:
            print("Error: No more questions in the list.")
        self.question_number += 1

        if current_question is not None:
            user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
            self.check_answer(user_answer, current_question.answer)
        else:
            print("Error: No current question available.")

    def check_answer(self, user_answer, correct_answer):
        """Check if the user's answer is correct."""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")

    def choose_question_category(self):
        """Choose the category of the quiz."""
        category_list = ['general knowledge', 'books', 'film', 'music', 'musicals & theatres', 'television', 'video games', 'board games', 'science & nature',
                         'computers', 'science: mathematics', 'mythology', 'sports', 'geography', 'history', 'politics', 'art', 'celebrities', 'animals', 'vehicles',
                         'comics', 'gadgets', 'japanese anime & manga', 'cartoon & animations']
        category = input(f"Choose category  General Knowledge, Books, Film, Music, Musicals & Theatres, Television, Video Games, Board Games, Science & Nature, "
                         f"Computers, Mathematics, Mythology, Sports, Geography, History, Politics, Art, Celebrities, Animals, Vehicles, Comics, Gadgets, "
                         f"Japanese Anime & Manga, Cartoon & Animations): ").lower()
        if category in category_list:
            print(f"You have chosen {category} category.")
        elif category_list != category:
            print("Invalid input. Please choose a valid category.")
        else:
            print("Invalid input. Please choose a valid category.")
        self.question_list = [question for question in self.question_list if question.category == category]
        return self.question_list


    def choose_difficulty_level(self):
        """Choose the difficulty level of the quiz."""
        difficulty_level = ['easy', 'medium', 'hard']
        level = input(f"Choose difficulty level ({', '.join(difficulty_level)}): ").lower()
        if level in difficulty_level:
            print(f"You have chosen {level} level.")
        elif difficulty_level != level:
            print("Invalid input. Please choose a valid difficulty level.")
        else:
            print("Invalid input. Please choose a valid difficulty level.")
        self.question_list = [question for question in self.question_list if question.difficulty == level]
        return self.question_list

