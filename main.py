from turtle import Screen, Turtle
from score import Score
from paddle import Paddle


def draw_line(t1):
    t1.hideturtle()
    t1.penup()
    t1.color('white')
    t1.goto(0, 290)
    t1.setheading(270)
    t1.pensize(5)
    for _ in range(57):
        if _ % 2 == 1:
            t1.pendown()
            t1.forward(10)
        else:
            t1.penup()
            t1.forward(10)


screen = Screen()
screen.setup(width=1000, height=600)
screen.title("Pingpong")
screen.bgcolor("Black")
screen.tracer(0)
t = Turtle()
draw_line(t)
paddle1 = Paddle(1)
paddle2 = Paddle(-1)


score1 = Score(-50, 250)
score2 = Score(50, 250)



while score1.score < 5 or score2.score < 5:



screen.update()

screen.exitonclick()
