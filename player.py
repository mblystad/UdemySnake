import turtle
import random

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10
colors = [
    "yellow", "gold", "orange", "red", "maroon",
    "violet", "magenta", "purple", "navy", "blue",
    "skyblue", "cyan", "turquoise", "lightgreen",
    "green", "darkgreen", "chocolate", "brown",
    "black", "gray"
]

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("circle")
        self.head.color("green")
        self.head.shapesize(1, 2, 1)
        self.new_segment = self.segments[-1]

    def create_snake(self):
        slangehode = [(0, 0), (-10, -5), (-20, 0), (-10, 5)]  # Eksempelkoordinater
        turtle.register_shape("slangehode", slangehode)

        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_segment = turtle.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.color(random.choice(colors))
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move_forward(self):
        self.head.forward(20)

    def turn_left(self):
        if self.head.heading() != 180 and self.head.heading() != 0:
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() != 180 and self.head.heading() != 0:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 90 and self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 270 and self.head.heading() != 90:
            self.head.setheading(270)
