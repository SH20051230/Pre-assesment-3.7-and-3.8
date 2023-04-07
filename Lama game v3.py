# imports
# In this version I have replaced the time.sleep method with a main game loop function
# to continue the game until the player clicks the "x" on the top right corner
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
# main game loop
# Maintain the game loop until the user click the "X"
quit_game = False
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
pygame.quit()
quit()
