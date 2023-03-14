from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super(Paddle, self).__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(1,5)
        self.penup()
        self.goto(0,-260)

    def move_right(self):
        if self.xcor() < 440:
            x = self.xcor()
            self.goto(x+20,-260)

    def move_left(self):
        if self.xcor() > -440:
            x = self.xcor()
            self.goto(x - 20, -260)