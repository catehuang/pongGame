from turtle import Turtle

FONT = ("Courier", 24, "normal")
FONT_BOLD = ("Courier", 32, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_score = 0
        self.computer_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 250)
        self.write("Computer vs. Player", align=ALIGNMENT, font=FONT)
        self.goto(-100, 200)
        self.write(self.computer_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.player_score, align=ALIGNMENT, font=FONT)

    def player_get_one_point(self):
        self.player_score += 1
        self.update_scoreboard()

    def computer_get_one_point(self):
        self.computer_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        if self.player_score == self.computer_score:
            self.write("Draw", align=ALIGNMENT, font=FONT_BOLD)
        elif self.player_score > self.computer_score:
            self.write("You win!", align=ALIGNMENT, font=FONT_BOLD)
        else:
            self.write("You lose!", align=ALIGNMENT, font=FONT_BOLD)