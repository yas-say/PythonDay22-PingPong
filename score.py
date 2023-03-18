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

    def score_increment(self):
        self.clear()
        self.score += 1
        self.write(self.score, move=False, align=ALIGNMENT, font=FONT)

    def game_over(self, str):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
        self.goto(0, -40)
        self.write(f"{str}", move=False, align=ALIGNMENT, font=FONT)