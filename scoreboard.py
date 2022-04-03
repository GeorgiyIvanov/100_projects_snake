from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        with open('record.txt', 'r') as f:
            self.high_score = int(f.readline()[-1])
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color('green')
        self.print_score()

    def update_score(self):
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('record.txt', 'w') as f:
                f.write(f'record: {self.high_score}')
        self.score = 0
        self.print_score()

    # def game_over(self):
    #     self.goto((0, 0))
    #     self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)

    def print_score(self):
        self.clear()
        self.goto((-70, 270))
        self.write(f"Score: {self.score}", False, align='center', font=FONT)
        self.goto((70, 270))
        self.write(f"Record: {self.high_score}", False, align='center', font=FONT)
