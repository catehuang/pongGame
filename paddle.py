from turtle import Turtle

PLAYER_MOVING_DISTANCE = 25
COMPUTER_MOVING_DISTANCE = 15


class Paddle(Turtle):

    def __init__(self, x_position, y_position):
        super().__init__()
        super().shape("square")
        super().shapesize(stretch_wid=5, stretch_len=1)
        super().color("white")
        self.x_position = x_position
        self.y_position = y_position
        self.penup()
        self.speed("fastest")
        self.goto(self.x_position, self.y_position)

    def move_up(self):
        if self.ycor() < 240:
            y_position = self.ycor() + PLAYER_MOVING_DISTANCE
            self.goto(self.x_position, y_position)

    def move_down(self):
        if self.ycor() > -240:
            y_position = self.ycor() - PLAYER_MOVING_DISTANCE
            self.goto(self.x_position, y_position)

    def move_up_computer(self):
        if self.ycor() < 240:
            y_position = self.ycor() + COMPUTER_MOVING_DISTANCE
            self.goto(self.x_position, y_position)

    def move_down_computer(self):
        if self.ycor() > -240:
            y_position = self.ycor() - COMPUTER_MOVING_DISTANCE
            self.goto(self.x_position, y_position)
