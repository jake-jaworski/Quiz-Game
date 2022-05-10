from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    question_text = q["text"]
    question_answer = q["answer"]
    new_question = Question(text=question_text, answer=question_answer)
    question_bank.append(new_question)

print(question_bank[0])
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"The quiz is complete. Your final score is {quiz.score}/{quiz.question_number}.\n")


