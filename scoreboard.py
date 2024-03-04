from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as self.file:
            self.highscore = int(self.file.read())
        self.goto(0, 250)
        self.color("white")
        self.refresh_score()

    # Refreshes snake game score
    def refresh_score(self):
        self.clear()
        self.write(f"Scoreboard: {self.score}, High Score:{self.highscore}", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    # Resets snake game
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as self.file:
                self.file.write(str(self.highscore))
        self.score = 0
        self.refresh_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over", move=False, align=ALIGNMENT, font=FONT)
