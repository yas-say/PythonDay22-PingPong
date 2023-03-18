from turtle import Turtle
from random import randint


class Puck(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("lime")
        self.speed("slowest")
        # self.refresh()

    # def move(self):
    #     self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def move(self):
        self.forward(20)

    def movewest(self):
        #input("movewest")
        self.setheading(randint(135, 225))
        self.move()


    def moveeast(self):
        #input("moveeast")
        angle1 = randint(315, 405)
        if angle1 > 360:
            angle1 = angle1 - 360
        self.setheading(angle1)
        self.move()

    def movenorth(self):
        #input("movenorth")
        print(f"heading now: {self.heading()}")
        #input("wait")

        if self.heading() in range(135,225):
            #input("going west")
            self.setheading(randint(135,180))
        else:
            self.setheading(randint(0,45))
            #input("going east")
        self.move()

    def movesouth(self):
        #input("movesouth")
        if self.heading() in range(135,225):
           # input("going west")
            self.setheading(randint(180,225))
        else:
          #  input("going east")
            self.setheading(randint(315,359))

    def reset(self, head):
        self.goto(0, 0)
        self.setheading(head)
