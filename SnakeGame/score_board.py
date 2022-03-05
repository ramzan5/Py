from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 280)
        self.penup()
        self.color('white')
        self.score_update()
        self.hideturtle()

    def score_update(self):
        self.write(f"Score: {self.score}", True, align="center", font=('Arial', 12, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("GameOVER", True, align="center", font=('Arial', 28, 'normal'))

    def score_increment(self):
        self.score += 1
        self.clear()
        self.score_update()


