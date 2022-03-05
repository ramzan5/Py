
class QuizBrain:
    def __init__(self,list):
        self.question_number = 0
        self.question_list = list
        self.score = 0


    def next_question(self):
       while self.question_number<(len(self.question_list)):
           q1 = input(f"q-{self.question_number} {self.question_list[self.question_number].text} (True/False) ")
           q1.lower()
           if q1 == self.question_list[self.question_number].answer.lower():
               self.score += 1
               print("You got correct answer")

           else:
               print("You got Wrong answer")


           print(f"Correct answer was {self.question_list[self.question_number].answer }")
           print(f"You got the scores {self.score}/{self.question_number + 1}")
           self.question_number +=1
