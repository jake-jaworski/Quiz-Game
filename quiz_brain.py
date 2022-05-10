class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_bank = question_bank
        self.score = 0

    def next_question(self):
        current_question = self.question_bank[self.question_number]
        self.question_number += 1
        player_answer = input(f"Q.{self.question_number}: {current_question.text} True or False? ")
        self.check_answer(player_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_bank)

    def check_answer(self, player_answer, correct_answer):
        if player_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your score is {self.score}/{self.question_number}.\n")

