from turtle import Turtle, Screen

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
LOWER_LIMIT = 0
STEP = -1

# In the snake game, if you're moving up, you can't move down instantly, and vice versa.
# Similarly, if you're heading left, you can't move to the right instantly, and vice versa.
# The constants above, together with the up(), down(), left(), right() methods will help us do this.


class Snake:
    """Create a snake using this class"""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # Head of the snake is at the 0th (first) index.

    def create_snake(self):
        #  Create snake body using 3 squares
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # Add the new segment to the last position of the segment.
        self.add_segment(self.segments[-1].position())  # Get hold og last position.

    def move(self):
        for seg_num in range(len(self.segments) - 1, LOWER_LIMIT, STEP):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)  # Move the head forward

    def up(self):
        # First check if snake's head is not moving down
        if self.head.heading() != DOWN:
            # Turn the head up
            self.head.setheading(UP)  # setheading() works with the reference at 0 degrees and goes anticlockwise.

    def down(self):
        # First check if snake's head is not moving up
        if self.head.heading() != UP:
            # Turn the head down
            self.head.setheading(DOWN)

    def left(self):
        # First check if snake's head is not moving towards right
        if self.head.heading() != RIGHT:
            # Turn the head left
            self.head.setheading(LEFT)

    def right(self):
        # First check if snake's head is not moving towards left
        if self.head.heading() != LEFT:
            # Turn the head right
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
