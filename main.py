from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Creates a screen object for the snake game
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
turtle_list = []

snake = Snake(turtle_list)
food = Food()

# Detects user keystrokes and calls functions to change snake heading accordingly.
screen.listen()
screen.onkey(fun=snake.snake_up, key="Up")
screen.onkey(fun=snake.snake_down, key="Down")
screen.onkey(fun=snake.snake_left, key="Left")
screen.onkey(fun=snake.snake_right, key="Right")

scoreboard = Scoreboard()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Detect collision with food

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.score += 1
        scoreboard.refresh_score()
        snake.add_segment()

    # Detect collision with wall

    if snake.segments[0].xcor() >= 300 or snake.segments[0].xcor() <= -300:
        scoreboard.reset()
        snake.reset_snake()
    elif snake.segments[0].ycor() >= 300 or snake.segments[0].ycor() <= -300:
        scoreboard.reset()
        snake.reset_snake()

    # Detect collision with tail

    if snake.tail_collision():
        scoreboard.reset()
        snake.reset_snake()

screen.mainloop()
