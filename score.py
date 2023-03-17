from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ('Verdana', 30, 'bold')


class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(x, y)
        self.write(self.score, move=False, align=ALIGNMENT, font=FONT)
