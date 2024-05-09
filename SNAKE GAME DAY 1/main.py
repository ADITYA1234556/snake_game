from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
scoreboard = ScoreBoard()
import time
snake = Snake()
screen = Screen()
food = Food()
screen.bgcolor("black")
screen.setup(width=660, height=660)
screen.title("WELCOME TO SNAKE GAME")
screen.tracer(0)

game_on = True
screen.listen()
screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_left, "Left")
screen.onkey(snake.snake_down, "Down")
screen.onkey(snake.snake_right, "Right")
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_follow()
    if snake.snake_list[0].distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend_snake()
    if snake.snake_list[0].xcor() > 300 or snake.snake_list[0].xcor() < -300 or snake.snake_list[0].ycor() > 300 or snake.snake_list[0].ycor() < -300:
        snake.reset()
        scoreboard.reset()
    for xyangles in snake.snake_list[1::]:
        if snake.snake_list[0].distance(xyangles) < 10:
            snake.reset()
            scoreboard.reset()


screen.exitonclick()