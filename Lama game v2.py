# imports
# In this version I have added the game icon and captions in it, and then test it to make sure it's working
import pygame
import time
pygame.init()
# get the screen dimensions
# I notice the 750 height is too big, that's overkill for this game, so I changed it to 400 to lower it.
screen = pygame.display.set_mode((1000, 400))
# load the game icon
game_icon = pygame.image.load("llama_icon.png")
# display the game icon
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Llama game by Steven-Huang")
# Set the time before the program close to see the screen
time.sleep(5)
pygame.quit()
quit()
