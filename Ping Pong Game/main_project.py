from turtle import Screen, Turtle
import paddle
import time
import ball
import score
import sound

scores = score.scoreboard()

bg_music = sound.Sound()
bg_music.bg_music()

# Screen Setup
screen = Screen()
screen.setup(height=1.0, width=1.0)
screen.bgpic(r"stuff\bgpic2.png")
screen.title("Pong Game")
screen.tracer(0)
right_paddle = paddle.Paddle("right")
left_paddle = paddle.Paddle("left")


# Borders
def draw_border():
    border = Turtle()
    border.fillcolor("white")
    border.color("#000080")
    border.penup()
    border.setpos(-500, 350)
    border.pensize(2)
    border.pendown()
    border.speed(6)
    for i in range(4):
        if i % 2:
            border.forward(700)
        else:
            border.forward(1000)
        border.right(90)
    border.ht()


draw_border()


# Starting The Game
# Countdown Timer

def countdown_timer(sleep_time):
    count = Turtle()
    for count2 in range(3):
        count3 = 3 - count2
        count.clear()
        count.color("#000080")
        count.write(count3, align="center", font=("Segoe UI", 100, "normal"))
        time.sleep(sleep_time)
    count.clear()
    count.hideturtle()


countdown_timer(0.6)
screen.update()

circle = ball.Ball()

game_is_on = True
while game_is_on:
    screen.listen()
    screen.onkeypress(right_paddle.up, "Up")
    screen.onkeypress(right_paddle.down, "Down")
    screen.onkeypress(left_paddle.up, "w")
    screen.onkeypress(left_paddle.down, "s")
    screen.tracer(0)
    screen.update()
    time.sleep(0.05)
    circle.move()
    circle.detect_collision()
    if circle.xcor() >= 510:
        countdown_timer(0.4)
        circle.reset()
        scores.lscore += 1
        scores.update_score()

    elif circle.xcor() <= -510:
        scores.rscore += 1
        scores.update_score()
        countdown_timer(0.4)
        circle.reset()

    if circle.xcor() >= 466 and circle.distance(right_paddle.paddy.xcor(), right_paddle.paddy.ycor()) < 50:
        circle.bounce('x')
        circle.i -= 0.001
        time.sleep(circle.i)
    if circle.xcor() <= -466 and circle.distance(left_paddle.paddy.xcor(), left_paddle.paddy.ycor()) < 50:
        circle.bounce('x')
        circle.i -= 0.001
        time.sleep(circle.i)

screen.exitonclick()
