# imports
# I have added the collision system dectecting if the player collide with the obsacles the game will end
# and also added scoring system that can record scores for eevry second the player lives
import pygame
import time
import random
import math
pygame.init()
clock = pygame.time.Clock()
obsacles = pygame.image.load("cactus.png")
Obesacle_moving = True
Speed_of_moving = 1
x = 80
y = 272

Score = 0
start_time = time.time()  # to record time from the start of the game
# fonts to be used
score_font = pygame.font.SysFont("arialblack", 20)
msg_font = pygame.font.SysFont("arialblack", 20)
def player_score(score, score_colour):
    display_score = score_font.render(f"Score: {score}", True, score_colour)
    screen.blit(display_score, (600, 10))

def message(msg, txt_colour, background_colour):
    txt = msg_font.render(msg, True, txt_colour, background_colour)
    text_box = txt.get_rect(center=(400, 200))
    screen.blit(txt, text_box)

# get the screen dimensions
# I notice the 750 height is too big, that's overkill for this game, so I changed it to 400 to lower it.
screen = pygame.display.set_mode((800, 400))
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
# The random obsacles x and y positions
obsacles_x = 500
obsacles_Y = 180
obsacles_x_change = 0
obsacles_collisions = False
obsacles_moving = False
X_gravity = 1
X_distance = 20
X_velocity = X_distance
obsacles_location = []
# Maintain the game loop until the user click the "X"
background_colour = white
background = pygame.image.load("ground.png")
screen.blit(pygame.transform.scale(background, (800, 600)), (0, 0))
quit_game = False
cactus_Speed = random.randint(10, 25)
time_start = time.time()
while not quit_game:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print(f"End Y_POSITION: {llama_y} and Y_VELOCITY is reset to JUMP_HEIGHT:{Y_VELOCITY}")
            quit_game = True
    cactusIMG = pygame.transform.scale(pygame.image.load('cactus.png'),
                                       (70, 70))

    if (math.dist((obsacles_x, obsacles_Y), (x, y)) < 50):
        cactus_x = 800
        cactus_y = 282
        time_start = time.time()
        break
    screen.blit(cactusIMG, (obsacles_x, obsacles_Y))
    obsacles_x -= cactus_Speed
    if (obsacles_x < -80):
        # Create a random speed for the cactus
        cactus_Speed = random.randint(10, 25)
        obsacles_x = 500
        obsacles_Y = 180
    timer = time.time()
    pygame.display.update()
    # checking if the player hits the cactus
    if llama_x == obsacles_x and llama_y == obsacles_Y:
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


    Score = round(time.time() - start_time)
    screen.fill(white)
    mario_rect = llama_rec.get_rect(center=(llama_x, llama_y))
    obsacles_rec = obsacles.get_rect(center=(obsacles_x, obsacles_Y))
    screen.blit(llama_rec, mario_rect)
    screen.blit(obsacles, obsacles_rec)
    screen.blit(background, (100, 110))
    player_score(Score, black)
    pygame.display.update()
    clock.tick(30)

message("you died", black, white)
pygame.display.update()
time.sleep(5)
pygame.quit()
quit()
