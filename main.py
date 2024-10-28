from turtle import *
import random
import time
from player import *
from food import *
from Scoreboard import *
import pygame

pygame.init()
pygame.mixer.init()

# Load the coin collection sound (replace 'coin_sound.wav' with your sound file's path)
coin_sound = pygame.mixer.Sound('food.wav')
game_over_sound = pygame.mixer.Sound('explosion.wav')
pygame.mixer.music.load('bgmusic.wav')

# Play the music
pygame.mixer.music.play(-1)  # The -1 makes the music loop indefinitely



# Stop the music and quit

# Function to simulate collecting a coin


screen = Screen()
kyll = 'kylling.gif'
screen.register_shape(kyll)
screen.bgcolor("white")
screen.setup(600, 600)
screen.title("Chicken Snakes")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
food.shape(kyll)
# Listen for key presses
screen.listen()
# Bind arrow keys
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
game_is_on = True

box_turtle = turtle.Turtle()
box_turtle.penup()
rectangle_width = 600
# Specify the height of the rectangle that covers the center of the screen
# Adjust this value as needed, example here uses 1/3 of the screen height
rectangle_height = 200

# Calculate starting position for the rectangle
# The rectangle should start from the left side and be centered vertically
start_x = -300  # Starting X coordinate (left side of the screen)
start_y = rectangle_height / 2  # Starting Y coordinate (centered vertically)

# Move to the starting position
box_turtle.goto(start_x, start_y)

box_turtle.pendown()
box_turtle.fillcolor("white")

def play_game_over_sound():
    game_over_sound.play()
def collect_coin():
    coin_sound.play()


def create_box():
    box_turtle.begin_fill()
    for _ in range(2):
        box_turtle.forward(rectangle_width)  # Draw the top side of the rectangle
        box_turtle.right(90)
        box_turtle.forward(rectangle_height)  # Draw the right side of the rectangle
        box_turtle.right(90)
    box_turtle.end_fill()
    box_turtle.hideturtle()


#     Detect collision with body and tail
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_increase()
        collect_coin()
        print(score)

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        txt = Score()
        txt.clear()
        create_box()
        txt.goto(0, 0)
        txt.write(arg=f'GAME OVER ', move=True, align=ALIGNMENT, font=FONT2)
        pygame.mixer.music.stop()
        play_game_over_sound()

    for segment in snake.segments[2:-1]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            txt = Score()
            txt.clear()
            create_box()
            box_turtle.begin_fill()
            txt.goto(0, 0)
            txt.write(arg=f'GAME OVER', move=True, align=ALIGNMENT, font=FONT2)
            pygame.mixer.music.stop()
            play_game_over_sound()

screen.exitonclick()
