# Space Invader
# Game developed by Subash khatri and Ram Kumar Shrestha
# 01/11/2022

import random
import turtle

# Setup the Screen
window = turtle.Screen()
window.bgcolor("black")
window.title("Invaders by Subash and Ram")
window.bgpic("background.gif")



# Register shape of players
turtle.register_shape("invader.gif")
turtle.register_shape("protector.gif")

# Draw Border
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.setposition(-300,-300)
border.pendown()
border.pensize(3)
for side in range(4):
    border.fd(600)
    border.lt(90)
border.hideturtle()

# Initial Score be 0
score = 0

# Draw the pen
draw_score = turtle.Turtle()
draw_score.speed(0)
draw_score.color("white")
draw_score.penup()
draw_score.setposition(-290, 280)
score_string = "Score: %s" %score
draw_score.write(score_string, False, align="left", font=("Arial", 14, "normal"))
draw_score.hideturtle()


# Create the player turtle
protector = turtle.Turtle()
#protector.color("blue")
protector.shape("protector.gif")
protector.penup()
protector.speed(0)
protector.setposition(0,-250)
protector.setheading(90)

protector_speed = 15

# Choose a number of invaders
number_of_invaders = 10
# Create an empty list of invaders
invaders = []

# Add invaders to the list
for i in range(number_of_invaders):
    # create the enemy
    invaders.append(turtle.Turtle())

for invader in invaders:
    #invader.color("Red")
    invader.shape("invader.gif")
    invader.penup()
    invader.speed(0)
    x = random.randint(-200, 200)
    y =  random.randint(100, 250)
    invader.setposition(x, y)

invader_speed = 5

# Create fire_balls for the protector to attack the invaders
fire_ball = turtle.Turtle()
fire_ball.color("red")
fire_ball.shape("triangle")
fire_ball.penup()
fire_ball.speed(2)
fire_ball.setheading(90)
fire_ball.shapesize(0.5,0.5)
fire_ball.hideturtle()

fire_ball_speed = 30

fire_ball_state = "ready"

#Move the player right and left

def move_left():
    x = protector.xcor()
    x -= protector_speed
    if x < -280:
        x -= 280
    protector.setx(x)

def move_right():
    x = protector.xcor()
    x += protector_speed
    if x > 280:
        x = 280
    protector.setx(x)

def fire_ball_action():
    global fire_ball_state

    if fire_ball_state == "ready":
        fire_ball_state = "fire"
        x = protector.xcor()
        y = protector.ycor() + 10
        fire_ball.setposition(x,y)
        fire_ball.showturtle()
        