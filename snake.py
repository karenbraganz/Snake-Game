from turtle import Turtle


class Snake:

    def __init__(self, segments):
        self.segments = segments
        self.create_turtles()
        self.create_snake()

    # Creates turtles that will form the initial snake body
    def create_turtles(self):
        for i in range(3):
            t = Turtle()
            t.penup()
            t.color("white")
            t.shape("square")
            self.segments.append(t)

    # Creates snake at starting position
    def create_snake(self):
        x = 0
        y = 0
        for i in self.segments:
            i.goto(x, y)
            x -= 20

    # Directs snake to move up
    def snake_up(self):
        turtle_heading = self.segments[0].heading()
        if turtle_heading != 270:
            self.segments[0].setheading(90)

    # Directs snake to move down
    def snake_down(self):
        turtle_heading = self.segments[0].heading()
        if turtle_heading != 90:
            self.segments[0].setheading(270)

    # Directs snake to move left
    def snake_left(self):
        turtle_heading = self.segments[0].heading()
        if turtle_heading != 0:
            self.segments[0].setheading(180)

    # Directs snake to move right
    def snake_right(self):
        turtle_heading = self.segments[0].heading()
        if turtle_heading != 180:
            self.segments[0].setheading(0)

    # Keeps the entire snake body moving cohesively in the same direction
    def move_snake(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(20)

    # Elongates snake body by appending a turtle object. This function is called when the snake collides with food.
    def add_segment(self):
        t = Turtle()
        t.penup()
        t.color("white")
        t.shape("square")
        self.segments.append(t)

    # Detects collision between snake head and tail
    def tail_collision(self):
        for i in range(2, len(self.segments)):
            if (self.segments[0].distance(self.segments[i]) < 10) and (self.segments[0].distance(self.segments[i]) < 10):
                print(i)
                return True

    # Resets snake to initial size and position. This is called when the snake collides with boundaries or its tail.
    def reset_snake(self):
        for i in self.segments:
            i.goto(1000, 1000)
        self.segments.clear()
        self.create_turtles()
        self.create_snake()




