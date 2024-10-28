from turtle import *
import random
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")
FONT2 = ("Courier", 28, "bold")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape("circle")
        self.penup()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto (0,265)
        self.write(arg=f'Score:{self.score}', move=True, align=ALIGNMENT, font=FONT)

    def score_increase(self):
        self.score += 1
        self.clear()
        self.goto (0,265)
        self.write(arg=f'Score:{self.score}', move=True, align=ALIGNMENT, font=FONT)

    def game_over(self):
        txt = Score()
        txt.goto(0, 0)
        txt.write(arg=f'GAME OVER. SCORE {self.score}: ', move=True, align=ALIGNMENT, font=FONT2)