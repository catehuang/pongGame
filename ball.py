from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        super().color("yellow")
        super().shape("circle")
        super().penup()
        self.generate_ball()
        self.x_move = 10
        self.y_move = 10

    def generate_ball(self):
        angle = random.randint(-80, 80)
        self.setposition(0, 0)
        self.setheading(angle)

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_by_wall(self):
        self.y_move *= -1

    def bounce_by_paddle(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_by_paddle()