from turtle import Turtle


# STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.segments = []
        self.create_paddle(x)
        self.head = self.segments[0]
        self.speed("fastest")

    def create_paddle(self, side):
        if side == 1:
            starting_position = [(470, 30), (470, 10), (470, -10)]
        elif side == -1:
            starting_position = [(-480, 30), (-480, 10), (-480, -10)]

        for position in starting_position:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def up(self):
        if self.segments[0].ycor() < 280:
            for _ in self.segments:
                _.goto(_.xcor(),_.ycor()+30)
    def down(self):
        if self.segments[-1].ycor() > -260:
            for _ in self.segments:
                _.goto(_.xcor(),_.ycor()-30)

    def w(self):
        if self.segments[0].ycor() < 280:
            for _ in self.segments:
                _.goto(_.xcor(),_.ycor()+30)
    def s(self):
        if self.segments[-1].ycor() > -260:
            for _ in self.segments:
                _.goto(_.xcor(),_.ycor()-30)