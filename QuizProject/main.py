
from data import question_data
from data import  Computer_data
from question import QuizModel
from quiz_brain import QuizBrain
print(Computer_data)
QuestionBank = [QuizModel(question_data[i]['text'],question_data[i]['answer']) for i in range(len(question_data))]
# print(QuestionBank)
print(len(QuestionBank))

quiz_brain = QuizBrain(QuestionBank)
quiz_brain.next_question()

