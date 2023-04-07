# imports
# This version I have added the jump method in order for my sprite to jump over obsacles
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
llama_rec = pygame.image.load("Llama.png")
# Jumping method
jumping = False # Starts out as false because Mario doesn't jump till space-bar pressed
# These are the 3 variables needed to make Mario jump
Y_GRAVITY = 1
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT
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
            print(f"End Y_POSITION: {llama_y} and Y_VELOCITY is reset to JUMP_HEIGHT:{Y_VELOCITY}")
            quit_game = True
    # This line returns a dictionary of all the keys which can be pressed, and whether or not they are being pressed
    keys_pressed = pygame.key.get_pressed()
    # This line checks that dictionary to see if the space bar is being pushed
    if keys_pressed[pygame.K_SPACE]:
     jumping = True  # So a jump is only happening if the space bar is pushed

    if jumping:
     print(f"Y_POSITION: {llama_y} because {Y_VELOCITY} - Y_GRAVITY (1)")
     llama_y -= Y_VELOCITY # This has the effect of moving Mario up the screen by 20px (see lines 15 and 16)
     Y_VELOCITY -= Y_GRAVITY # This has the effect of reducing each step by 1px (20,19...3,2,1,0,-1,-2,-3...-19,-20)
     if Y_VELOCITY < -JUMP_HEIGHT: # When Y_VELOCIY drops under -20
      jumping = False
      Y_VELOCITY = JUMP_HEIGHT # Resets Y_VELOCITY to 20

     # Reset Mario on JUMPING_SURFACE - while jumping
      mario_rect = llama_rec.get_rect(center=(llama_x, llama_y))
      screen.blit(llama_rec, mario_rect)

    #else:
     # Reset Mario on STANDING_SURFACE - when not jumping 05/01/2023, 08:24 c:\...\ZMario jumping tutorial - own\mario_v2 jumping only.py localhost:55070/db58f883-2334-4b49-88cf-06678326b58a/ 2/2
    #mario_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
    #SCREEN.blit(STANDING_SURFACE, mario_rect)

    screen.fill(white)
    pygame.draw.rect(screen, red, [llama_x, llama_y, 20, 20])
    screen.blit(background, (100, 110))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
