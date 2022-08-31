import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreBoard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)    # turn off animation

player = Paddle(370, 0)
computer = Paddle(-380, 0)
ball = Ball()
scoreBoard = Scoreboard()

is_game_on = True
INITIAL_SPEED_RATE = 0.1
speed_rate = INITIAL_SPEED_RATE

while is_game_on:
    screen.update()
    time.sleep(speed_rate)
    ball.move()
    screen.listen()
    screen.onkeypress(player.move_up, "Up")
    screen.onkeypress(player.move_down, "Down")

    # bounce by upper wall or bottom wall (y direction)
    if ball.ycor() > 260 or ball.ycor() < -260:
        ball.bounce_by_wall()

    # computer actions
    if ball.x_move < 0 and ball.xcor() < -200:
        computer_top = computer.ycor() + 50
        computer_bottom = computer.ycor() - 50
        # the radius of a ball is 10; the height of a paddle is 100 in total
        if ball.ycor() - 10 > computer_top:
            computer.move_up_computer()
        elif ball.ycor() + 10 < computer_bottom:
            computer.move_down_computer()
    # moves back to the y-center after hit ball
    elif ball.x_move > 0 and ball.xcor() < -200:
        if computer.ycor() > 0:
            computer.move_down_computer()
        else:
            computer.move_up_computer()

    # hit by paddles (x direction)
    if ball.xcor() > 340 and player.ycor() - 50 <= ball.ycor() <= player.ycor() + 50 or \
       ball.xcor() < -340 and computer.ycor() - 50 <= ball.ycor() <= computer.ycor() + 50:
        if ball.xcor() < 360 or ball.xcor() < -370:
            ball.bounce_by_paddle()
            speed_rate /= 1.5

    if ball.xcor() > 390:
        scoreBoard.computer_get_one_point()
        ball.reset_ball()
        speed_rate = INITIAL_SPEED_RATE

    if ball.xcor() < -390:
        scoreBoard.player_get_one_point()
        ball.reset_ball()
        speed_rate = INITIAL_SPEED_RATE

    if scoreBoard.player_score > 4 or scoreBoard.computer_score > 4:
        is_game_on = False
        scoreBoard.game_over()


screen.exitonclick()