from turtle import Turtle
from random import randint

class Puck(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("lime")
        self.speed("fastest")
        # self.refresh()

    # def move(self):
    #     self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def move(self):
        self.forward(10)

    def moveback(self):
        ang = randint(10,80)
        self.setheading(ang)
        self.move()
