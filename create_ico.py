from PIL import Image
import os

# Open the PNG image
img = Image.open("assets/images/game_logo.png")

# Create ICO file
img.save("game_icon.ico", format='ICO')
