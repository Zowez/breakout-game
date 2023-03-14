from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.refresh()

    def refresh(self):
        self.setx(0)
        self.sety(-240)
        self.x_move = 5
        self.y_move = 5

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1
        print("sekti")

    def bounce_y(self):
        self.y_move *= -1