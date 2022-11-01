# Space Invader
# Game developed by Subash khatri and Ram Kumar Shrestha
# 01/11/2022

import turtle

# Setup the Screen
window = turtle.Screen()
window.bgcolor("black")
window.title("Invaders by Subash and Ram")
window.bgpic("background.gif")



# Register shape of players
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

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

