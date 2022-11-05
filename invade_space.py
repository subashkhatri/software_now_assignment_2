# Space Invader
# Game developed by Subash khatri and Ram Kumar Shrestha
# 01/11/2022

import math
import random
import turtle

# Setup the Screen
window = turtle.Screen()
window.bgcolor("black")
window.title("Invaders by Subash & Ram")
window.bgpic("background.gif")


# Register shape of protectors
turtle.register_shape("invader.gif")
turtle.register_shape("protector.gif")

# Draw Border
border = turtle.Turtle()
border.speed(0)
border.color("red")
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


# Create the protector turtle
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
    # create the invader
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
fire_ball.shape("circle")
fire_ball.penup()
fire_ball.speed(0)
fire_ball.setheading(90)
fire_ball.shapesize(0.5,0.5)
fire_ball.hideturtle()

fire_ball_speed = 30

fire_ball_state = "ready"

#Move the protector right and left

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


# For collision between invader and fire_ball
def is_collision_invader_fire_ball(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 25:
        return True
    else:
        return False

# For collision between invader and protector
def is_collision_invader_protector(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 30:
        return True
    else:
        return False


# Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_ball_action, "space")

# Main game loop
Game_Over = False
missed_invaders = 0
while True:

    for invader in invaders:
        # Move the invader
        x = invader.xcor()
        x += invader_speed
        invader.setx(x)


        # Move the invader back and down
        if invader.xcor() > 270:
            # Move all invaders down
            for e in invaders:
                y = e.ycor()
                y -= 40
                e.sety(y)
                if e.ycor() < -285 and Game_Over == False:
                    e.hideturtle()
                    missed_invaders += 1
                    if missed_invaders == 5:
                        Game_Over = True
                    x = random.randint(-200, 200)
                    y = random.randint(100, 250)
                    e.setposition(x, y)
                    e.showturtle()
            # Change invader direction
            invader_speed *= -1

        if invader.xcor() < -270:
            # Move all invaders down
            for e in invaders:
                y = e.ycor()
                y -= 40
                e.sety(y)
                if e.ycor() < -285 and Game_Over == False:
                    e.hideturtle()
                    missed_invaders += 1
                    if missed_invaders ==5:
                        Game_Over = True
                    x = random.randint(-200, 200)
                    y = random.randint(100, 250)
                    e.setposition(x, y)
                    e.showturtle()
            # Change invader direction
            invader_speed *= -1

        # check for a collision between the fire_ball and the invader
        if is_collision_invader_fire_ball(fire_ball, invader):
            # Reset the fire_ball
            fire_ball.hideturtle()
            fire_ball_state = "ready"
            fire_ball.setposition(0, -400)
            # Reset the invader
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            invader.setposition(x, y)
            invader_speed += 0.5
            # update the score
            score += 10
            score_string = "Score: %s" %score
            draw_score.clear()
            draw_score.write(score_string, False, align="center", font=("Arial", 14, "normal"))
        # check for a collision between the protector and invader
        if is_collision_invader_protector(protector, invader):
            Game_Over = True
        if Game_Over == True:
            protector.hideturtle()
            fire_ball.hideturtle()
            for e in invaders:
                e = turtle.Turtle()
                e.speed(0)
                e.penup()
                e.hideturtle()
                e.goto(0,0)
                e.write("Press ESC to exit the game")
                window.listen()
                window.onkeypress(window.bye, "Escape")
            window.bgpic("end.gif")
            break

    # Move the fire_ball
    if fire_ball_state == "fire":
        y = fire_ball.ycor()
        y += fire_ball_speed
        fire_ball.sety(y)

    # Check to see if the fire_ball has gone to the top
    if fire_ball.ycor() > 275:
        fire_ball.hideturtle()
        fire_ball_state = "ready"
