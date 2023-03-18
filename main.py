from turtle import Screen, Turtle
from score import Score
from paddle import Paddle
from puck import Puck
from time import sleep



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
puck_new = Puck()

score1 = Score(-50, 250)
score2 = Score(50, 250)
flag = True


screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.w, "w")
screen.onkey(paddle2.s, "s")


while flag:

    sleep(0.1)
    screen.update()
    puck_new.move()
    print(f"x= {puck_new.xcor()}, y={puck_new.ycor()}")
    print(f"Heading= {puck_new.heading()}")
    #input()
    for _ in paddle1.segments:
        if puck_new.distance(_)<30:
            puck_new.movewest()
    for _ in paddle2.segments:
        if puck_new.distance(_)<30:
            puck_new.moveeast()
    if puck_new.ycor() >= 260:
        # input()
        puck_new.movesouth()
    if puck_new.ycor() <= -260:
        puck_new.movenorth()
    if puck_new.xcor() > 490:
        score1.score_increment()
        puck_new.reset(180)
    if puck_new.xcor() < -495:
        score2.score_increment()
        puck_new.reset(0)
    if score1.score == 2:
        score1.game_over("Player 1 wins")
        flag = False
    if score2.score == 2:
        score2.game_over("Player 2 wins")
        flag = False


screen.exitonclick()

