from turtle import Turtle, Screen
import pygame
import sound

screen = Screen()
user1_input = screen.textinput("Enter Player Name", "Player 1: ")
user2_input = screen.textinput("Enter Player Name", "Player 2: ")


class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("#B1BDE6")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.goto(0, 260)
        self.write("SCOREBOARD", align="center", font=("Anurati", 45, "normal"))
        self.goto(-100, 220)
        self.write(user1_input + " : " + str(self.lscore), align="center", font=("Segoe UI", 20, "normal"))
        self.goto(100, 220)
        self.write(user2_input + " : " + str(self.rscore), align="center", font=("Segoe UI", 20, "normal"))

    def update_score(self):
        self.clear()
        self.goto(0, 260)
        self.write("SCOREBOARD", align="center", font=("Anurati", 43, "normal"))
        self.goto(-100, 220)
        self.write(user1_input + " : " + str(self.lscore), align="center", font=("Segoe UI", 20, "normal"))
        self.goto(100, 220)
        self.write(user2_input + " : " + str(self.rscore), align="center", font=("Segoe UI", 20, "normal"))
        if self.lscore >= 5 or self.rscore >= 5:
            self.color("#000080")
            self.goto(0, 0)
            if self.lscore >=5 :
                self.write(f"{user1_input} WON", align="center", font=("Anurati", 50, "normal"))
            else:
                self.write(f"{user2_input} WON", align="center", font=("Anurati", 50, "normal"))
            over = sound.Sound()
            over.game_over()
            pygame.time.wait(10000)
            pygame.quit()
