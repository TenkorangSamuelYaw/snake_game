from turtle import Turtle
COLOR = "white"
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
X_POSITION = 0
Y_POSITION = 270


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        #  First open the data file, and read the contents in into self.high_score
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color(COLOR)
        self.penup()
        self.goto(x=X_POSITION, y=Y_POSITION)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()  # clear current score on the screen.
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            #  Now write the contents to the data.txt file
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1  # Score updated in memory, but not on screen yet.
        self.update_scoreboard()  # Before updating the screen with the new score.
