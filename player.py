from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("#a0a0f0")
        self.pencolor("#5ea2e6")
        self.penup()
        self.setheading(90)
        self.setpos(STARTING_POSITION)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)
