# Space Invader
# Game developed by Subash khatri and Ram Kumar Shrestha
# 01/11/2022

import turtle

# Setup the Screen
window = turtle.Screen()
window.bgcolor("white")
window.title("Invaders by Subash and Ram")
window.bgpic("background.gif")



# Register shape of players
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

# Draw Border

# Initial Score be 0
