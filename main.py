from turtle import Screen,Turtle
from paddle import Paddle
import time
from map import Map
from ball import Ball

screen = Screen()
screen.setup(width=960, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

score_v = 0
score = Turtle()
score.penup()
score.hideturtle()
score.goto(-300, 240)
score.color("white")

heart_v = 3
heart = Turtle()
heart.penup()
heart.hideturtle()
heart.goto(300,240)
heart.color("red")

player = Paddle()
map = Map()
screen.listen()
ball = Ball()

screen.onkeypress(fun=player.move_left, key="Left")
screen.onkeypress(fun=player.move_right, key="Right")

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.01)

    ball.move()

    if ball.xcor() > 460 or ball.xcor() < -460:
        ball.bounce_x()

    if ball.ycor() == 280:
        ball.bounce_y()

    if ball.ycor() == player.ycor() + 20 and abs(ball.xcor() - player.xcor()) < 60:
        if abs(ball.xcor() - player.xcor()) < 60:
            ball.x_move = 7
            ball.y_move = -3
            if abs(ball.xcor() - player.xcor()) < 40:
                    ball.x_move = 5
                    ball.y_move = -5
                    if abs(ball.xcor() - player.xcor()) < 20:
                        ball.x_move = 3
                        ball.y_move = -7
        if(player.xcor() > ball.xcor()):
            ball.x_move *= -1


        ball.bounce_y()
        time.sleep(0.01)

    if ball.ycor() < -290:
        ball.refresh()
        heart_v -= 1

    for seg in map.segment_yellow:
        if seg.xcor() + 40 > ball.xcor() > seg.xcor() - 40 and abs(ball.ycor() - seg.ycor()) < 20:
            ball.bounce_y()
            seg.hideturtle()
            map.segment_yellow.remove(seg)
            score_v += 1
            break

        if abs(ball.xcor() - seg.xcor()) < 50 and seg.ycor() - 10 < ball.ycor() < seg.ycor() + 10:
            ball.bounce_x()
            seg.hideturtle()
            map.segment_yellow.remove(seg)
            score_v +=1
            break

    for seg in map.segment_orange:
        if seg.xcor() + 40 > ball.xcor() > seg.xcor() - 40 and abs(ball.ycor() - seg.ycor()) < 20:
            ball.bounce_y()
            seg.hideturtle()
            map.segment_orange.remove(seg)
            score_v += 1
            break

        if abs(ball.xcor() - seg.xcor()) < 50 and seg.ycor() - 10 < ball.ycor() < seg.ycor() + 10:
            ball.bounce_x()
            seg.hideturtle()
            map.segment_orange.remove(seg)
            score_v +=1
            break

    for seg in map.segment_green:
        if seg.xcor() + 40 > ball.xcor() > seg.xcor() - 40 and abs(ball.ycor() - seg.ycor()) < 20:
            ball.bounce_y()
            seg.hideturtle()
            map.segment_green.remove(seg)
            score_v += 1
            break

        if abs(ball.xcor() - seg.xcor()) < 50 and seg.ycor() - 10 < ball.ycor() < seg.ycor() + 10:
            ball.bounce_x()
            seg.hideturtle()
            map.segment_green.remove(seg)
            score_v +=1
            break

    for seg in map.segment_red:
        if seg.xcor() + 40 > ball.xcor() > seg.xcor() - 40 and abs(ball.ycor() - seg.ycor()) < 20:
            ball.bounce_y()
            seg.hideturtle()
            map.segment_red.remove(seg)
            score_v += 1
            break

        if abs(ball.xcor() - seg.xcor()) < 50 and seg.ycor() - 10 < ball.ycor() < seg.ycor() + 10:
            ball.bounce_x()
            seg.hideturtle()
            map.segment_red.remove(seg)
            score_v +=1
            break

    if heart_v == 0:
        game_is_on = False
        game_over = Turtle()
        game_over.penup()
        game_over.hideturtle()
        game_over.color("blue")
        game_over.write("GAME OVER!",align="center", font=("Courier", 60, "bold"))


    score.clear()
    heart.clear()
    score.write(f"Score:{score_v}", align="center", font=("Courier", 40, "normal"))
    heart.write(f"Heart:{heart_v}", align="center", font=("Courier", 40, "normal"))


screen.exitonclick()