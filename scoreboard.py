from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto((0, 270))
        self.score = 0
        self.color('green')
        self.print_score()

    def update_score(self):
        self.score += 1

    def game_over(self):
        self.goto((0, 0))
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
