import pygame
import time
import random
from random import randint
pygame.init()  # Initialises (starts) all pygame modules

Width = 1000
Height = 750

screen = pygame.display.set_mode((Width, Height))  # Creates a surface
game_icon = pygame.image.load('game_icon.png')  # Loads the icon
pygame.display.set_icon(game_icon)  # Displays the icon
pygame.display.set_caption("Race Game by Ezray")  # Displays Caption

White = (255, 255, 255)  # Colour of screen 
Black = (0, 0, 0)  # Colour of track lines
Green = (0, 128, 0)  # Colour of enemy car
Red = (255, 0, 0)  # Colour of obstacle

font = pygame.font.Font("freesansbold.ttf", 50)

# Car details
carX = 450
carY = 550
car_width = 50
car_height = 60
vel = 5

# Score system
score = 0
score_incease = 1

# Co-ordinates for obstacles
obs_width = 50
obs_height = 60
obsX1 = 350
obsX2 = 450
obsX3 = 550
obsX4 = 650
obsY1 = -100
obsY2 = -100
obsY3 = -100
obsY4 = -100
obsY1_change = 0
obsY2_change = 0
obsY3_change = 0
obsY4_change = 0

def player():
    # Draws a square(car) 
    player = pygame.draw.rect(screen, Green, [carX, carY, car_width, car_height])

def obstacles():
    # Draws a square(obstacles)
    obstacle_1 = pygame.draw.rect(screen, Red, [obsX1, obsY1, obs_width, obs_height])
    obstacle_2 = pygame.draw.rect(screen, Red, [obsX2, obsY2, obs_width, obs_height])
    obstacle_3 = pygame.draw.rect(screen, Red, [obsX3, obsY3, obs_width, obs_height])
    obstacle_4 = pygame.draw.rect(screen, Red, [obsX4, obsY4, obs_width, obs_height])

def track():
    # Draws the track lines
    pygame.draw.line(screen, Black, (320,0), (320,750))
    pygame.draw.line(screen, Black, (420,0), (420,750))
    pygame.draw.line(screen, Black, (520,0), (520,750))
    pygame.draw.line(screen, Black, (620,0), (620,750))
    pygame.draw.line(screen, Black, (720,0), (720,750))

def message(msg, text_colour, bkgd_colour):
    # Allows message to be created
    txt = font.render(msg, True, text_colour, bkgd_colour)
    text_box = txt.get_rect(center = (500,360))
    screen.blit(txt, text_box)

# Random speeds of the obstacles
obsY1_change = random.randint(4,8)
obsY2_change = random.randint(4,8)
obsY3_change = random.randint(4,8)
obsY4_change = random.randint(4,8)

clock = pygame.time.Clock()  # tick speed

quit_game = False  # Variable to start main loop 

# Main loop
while not quit_game:  

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  # Allows user to quit the game 
            quit_game = True  # Quits (stops) all pygame modules
        # Obstacles will move once keys have been pressed
    
    keys = pygame.key.get_pressed()  # Variable for pressing keys

    # car goes left when left key is pressed
    if keys[pygame.K_LEFT] and  carX > 320:
        carX -= vel
    # car goes right when left key is pressed
    elif keys[pygame.K_RIGHT] and carX < 670:
        carX += vel
    
    # Continuous speed of obstacles
    obsY2 += obsY2_change
    obsY3 += obsY3_change
    obsY4 += obsY4_change

    screen.fill(White)  # Fills the screen with a colour

    track()

    obstacles()

    player()

    # Collision with player and obstacles 
    if carY < obsY1 and carX <= obsX1:
        quit_game = True
    elif carY < obsY2 and carX <= obsX2:
        quit_game = True
    elif carY < obsY3 and carX <= obsX3:
        quit_game = True
    elif carY < obsY4 and carX <= obsX4:
        quit_game = True

    clock.tick(50)  # Tick speed

    pygame.display.update()  # Updates code above

message("You died!", White, Black) # Displays message
pygame.display.update()

pygame.quit()  # Quits (stops) all pygame modules
quit()  # Quits the app

