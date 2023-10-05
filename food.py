from turtle import Turtle
from random import randint
SPEED = "fastest"
COLOR = "green"
SHAPE = "circle"


class Food(Turtle):
    """Generate food for the snake using this class."""
    def __init__(self):
        # super(Food, self).__init__()
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # 10 x 10 pixel
        self.color(COLOR)
        self.speed(SPEED)
        self.refresh()

    # Move food to a new random location.
    def refresh(self):
        random_x = randint(-280, 260)
        random_y = randint(-280, 260)
        self.goto(random_x, random_y)

