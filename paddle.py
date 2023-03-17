from turtle import Turtle


# STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.segments = []
        self.create_paddle(x)
        self.head = self.segments[0]

    def create_paddle(self, side):
        if side == 1:
            print("here")
            starting_position = [(470, 30), (470, 10), (470, -10)]
        elif side == -1:
            print("there")
            starting_position = [(-480, 30), (-480, 10), (-480, -10)]

        for position in starting_position:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)
