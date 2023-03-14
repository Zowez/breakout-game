from turtle import Turtle

YELLOW_LEVEL_Y = 0
GREEN_LEVEL_Y = 40
ORANGE_LEVEL_Y = 80
RED_LEVEL_Y = 120
COUNT = 24
STARTING_POS_X = -450


class Map(Turtle):
    def __init__(self):
        super().__init__()
        self.map = Turtle("square")
        self.map.shapesize(1,5)
        self.map.penup()
        self.segment_yellow = []
        self.segment_green = []
        self.segment_orange = []
        self.segment_red = []
        self.level_yellow()
        self.level_green()
        self.level_orange()
        self.level_red()



    def level_yellow(self):

        x = STARTING_POS_X
        y = YELLOW_LEVEL_Y
        n = 0
        c = COUNT
        while c != 0:

            if n == 12:
                y = 20
                x = STARTING_POS_X

            new_yellow = Turtle("square")
            new_yellow.color("yellow")
            new_yellow.shapesize(0.9,3.8)
            new_yellow.penup()
            new_yellow.goto(x, y)
            self.segment_yellow.append(new_yellow)

            x += 80
            n +=1
            c -= 1


    def level_green(self):

        x = STARTING_POS_X
        y = GREEN_LEVEL_Y
        n = 0
        c = COUNT
        while c != 0:

            if n == 12:
                y = 60
                x = STARTING_POS_X

            new_green = Turtle("square")
            new_green.color("green")
            new_green.shapesize(0.9,3.8)
            new_green.penup()
            new_green.goto(x, y)
            self.segment_green.append(new_green)

            x += 80
            n +=1
            c -= 1

    def level_orange(self):

        x = STARTING_POS_X
        y = ORANGE_LEVEL_Y
        n = 0
        c = COUNT
        while c != 0:

            if n == 12:
                y = 100
                x = STARTING_POS_X

            new_orange = Turtle("square")
            new_orange.color("orange")
            new_orange.shapesize(0.9,3.8)
            new_orange.penup()
            new_orange.goto(x, y)
            self.segment_orange.append(new_orange)

            x += 80
            n +=1
            c -= 1

    def level_red(self):

        x = STARTING_POS_X
        y = RED_LEVEL_Y
        n = 0
        c = COUNT
        while c != 0:

            if n == 12:
                y = 140
                x = STARTING_POS_X

            new_red = Turtle("square")
            new_red.color("red")
            new_red.shapesize(0.9,3.8)
            new_red.penup()
            new_red.goto(x, y)
            self.segment_red.append(new_red)

            x += 80
            n +=1
            c -= 1