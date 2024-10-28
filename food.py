from turtle import Screen, Turtle
import random

# Create a screen object
# Register the image with the screen before using



class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape()  # Set the turtle's shape to the registered image
        self.penup()
        self.shapesize(10.5)  # This might not affect the image. Adjust the image size beforehand if needed.
        self.color("blue")  # Color may not be visible if using an image as the shape
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


# Make sure to initialize your Food class after the screen setup and shape registration



