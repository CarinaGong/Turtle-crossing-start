from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(-240, 260)
        self.color("black")
        self.level_up()

    def level_up(self):
        self.clear()
        Scoreboard.score += 1
        self.write(f"Level: {Scoreboard.score}", False, "center", FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.color("#5ea2e6")
        self.write("Game Over 👻", True, "center", FONT)
