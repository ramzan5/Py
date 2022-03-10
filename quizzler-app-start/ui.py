from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz:QuizBrain):
        self.screen = Tk()
        self.quiz = quiz
        self.screen.title("Quizlet")
        self.screen.config(padx=20,pady=20, bg=THEME_COLOR)
        self.score_placer = Label(text="Score:0/0",font=('Arail',16),fg='white')
        self.score_placer.config(padx=20,pady=20)
        self.score_placer.grid(row=0,column=1)
        self.canvas = Canvas(width=300,height=250,bg='white')
        self.question_text = self.canvas.create_text(150,125,width=270,text='SOME QUESTIONS',fill=THEME_COLOR)
        self.canvas.grid(row=1,column=0, columnspan=2,pady=30)
        correct = PhotoImage(file='images/true.png')
        self.correct = Button(image=correct,highlightthickness=0, command=self.true_pressed)
        self.correct.grid(row=2,column=0)
        wrong = PhotoImage(file='images/false.png')
        self.wrong = Button(image=wrong,highlightthickness=0,command=self.false_pressed)
        self.wrong.grid(row=2,column=1)
        self.get_next_question()
        self.screen.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_placer.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the End")
            self.correct.config(state="disabled")
            self.wrong.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg='red')
        self.screen.after(1000, self.get_next_question)


