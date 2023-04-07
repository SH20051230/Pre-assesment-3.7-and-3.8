# imports
# In this version I have initialised the llama and with the ground it will stand on
# with the clock that set the fps of the game
import pygame
import time
pygame.init()
clock = pygame.time.Clock()
# get the screen dimensions
# I notice the 750 height is too big, that's overkill for this game, so I changed it to 400 to lower it.
screen = pygame.display.set_mode((1000, 400))
# load the game icon
game_icon = pygame.image.load("llama_icon.png")
# display the game icon
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Llama game by Steven-Huang")
# The llama position
llama_x = 100
llama_y = 180
# main game loop
# colours used in the game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (188, 227, 199)
yellow = (255, 255, 0)
# Maintain the game loop until the user click the "X"
background_colour = white
background = pygame.image.load("ground.png")
quit_game = False
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
    screen.fill(white)
    pygame.draw.rect(screen, red, [llama_x, llama_y, 20, 20])
    screen.blit(background, (100, 110))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
