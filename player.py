from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.penup()


    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def go(self):
        self.forward(MOVE_DISTANCE)
