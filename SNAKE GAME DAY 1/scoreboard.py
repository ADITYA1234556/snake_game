from turtle import Turtle
ALIGNMENT = "right"
FONT = ("courier", 14, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("E:/PYTHON NEW/DAY 20/SNAKE GAME DAY 1/data.txt") as data:
           self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 290)
        self.score_title()

    def score_title(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("E:/PYTHON NEW/DAY 20/SNAKE GAME DAY 1/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
    def increase_score(self):
        self.score += 1
        self.goto(0, 290)
        self.score_title()


