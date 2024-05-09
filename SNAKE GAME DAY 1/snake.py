from turtle import  Turtle
import random

COLORS = ["red", "green", "blue", "pink"]
POSITION = [(0,0), (-20,0), (-40,0), (-60,0)]
MOVE = 20
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snakes()
    def create_snakes(self):
        for new_turtles in range(len(COLORS)):
            turtle = Turtle("turtle")
            turtle.color(COLORS[new_turtles])
            turtle.penup()
            turtle.goto(POSITION[new_turtles])
            self.snake_list.append(turtle)
    def reset(self):
        for snakes in self.snake_list:
            snakes.goto(500,500)
        self.snake_list.clear()
        self.create_snakes()
    def extend_snake(self):
        turtle = Turtle("turtle")
        turtle.color(random.choice(COLORS))
        turtle.penup()
        turtle.goto(self.snake_list[-1].position())
        self.snake_list.append(turtle)
    def snake_follow(self):
        for follow in range(len(self.snake_list) - 1, 0, -1):
            x_pos = self.snake_list[follow - 1].xcor()
            y_pos = self.snake_list[follow - 1].ycor()
            self.snake_list[follow].goto(x_pos, y_pos)
        self.snake_list[0].forward(MOVE)
    def snake_up(self):
        if self.snake_list[0].heading() != DOWN:
            self.snake_list[0].setheading(UP)
    def snake_left(self):
        if self.snake_list[0].heading() != RIGHT:
            self.snake_list[0].setheading(LEFT)
    def snake_right(self):
        if self.snake_list[0].heading() != LEFT:
            self.snake_list[0].setheading(RIGHT)
    def snake_down(self):
        if self.snake_list[0].heading() != UP:
            self.snake_list[0].setheading(DOWN)