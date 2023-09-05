from turtle import Turtle
import sound


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.i = 0.05
        self.shape("circle")
        self.speed('fast')
        self.pencolor("black")
        self.fillcolor("#960BEB")
        self.penup()
        self.setpos(0, 0)
        self.x_val = 10
        self.y_val = 10

    def move(self):
        new_x = self.xcor() + self.x_val
        new_y = self.ycor() + self.y_val
        self.goto(new_x, new_y)

    def detect_collision(self):
        if self.ycor() >= 350 or self.ycor() <= -350:
            self.bounce('y')

    def reset(self):
        self.goto(0, 0)
        self.bounce('x')
        self.speed('normal')
        self.i = 0.05
        lose_sound = sound.Sound()
        lose_sound.game_lose()

    def bounce(self, resp):
        if resp == 'y':
            self.y_val *= -1
        else:
            self.x_val *= - 1
        coll = sound.Sound()
        coll.collision()
