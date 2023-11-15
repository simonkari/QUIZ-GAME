from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Create an empty list to store Question objects
question_bank = []

# Iterate through the question_data and create Question objects, then add them to the question_bank list
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Create a QuizBrain object with the populated question_bank list
quiz = QuizBrain(question_bank)

# Create a QuizInterface object, passing the quiz object for user interaction
interface = QuizInterface(quiz)
