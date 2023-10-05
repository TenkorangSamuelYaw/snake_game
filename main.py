from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)  # Don't show anything on the screen.
starting_position = [(0, 0), (-20, 0), (-40, 0)]

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()  # Start listening for keystrokes.
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.3)
    snake.move()
    #  Detect collision with food.
    # Check to see if  the distance from the first segment(head) of snake to the food object is < 15. food is (10 x 10)
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()  # Once you find food, increase score by 1.
    #  Detect collision with the walls.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    #  Detect collision with tail.
    # We are not interested in the first segment [0], because it's the head.
    for segment in snake.segments[1:]:  # Get every segment aside the head from the beginning to the end.
        # See if the distance between the head and the current segment is < 10, and end the game.
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
