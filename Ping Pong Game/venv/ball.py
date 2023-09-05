from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.setpos(0, 0)
        self.x_val = 10
        self.y_val = 10

    def move(self):
        new_x = self.xcor() + self.x_val
        new_y = self.ycor() + self.y_val
        self.goto(new_x, new_y)

    def detect_collision(self):
        if self.ycor() >= 310 or self.ycor() <= -310:
            self.bounce('y')

    def reset(self):
        self.goto(0, 0)
        self.bounce('x')

    def bounce(self, resp):
        if resp == 'y':
            self.y_val *= -1
        else :
            self.x_val *= - 1





