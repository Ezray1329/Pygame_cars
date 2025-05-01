import pygame
import time
import random
pygame.init()  # Initialises (starts) all pygame modules

screen = pygame.display.set_mode((1000, 750))  # Creates a surface
game_icon = pygame.image.load('game_icon.png')  # Loads the icon
pygame.display.set_icon(game_icon)  # Displays the icon
pygame.display.set_caption("Race Game by Ezray")  # Displays Caption

White = (255, 255, 255)  # Colour of screen 
Black = (0, 0, 0)  # Colour of track lines
Green = (0, 128, 0)  # Colour of enemy car
Red = (255, 0, 0)  # Colour of car

clock = pygame.time.Clock()  # tick speed

quit_game = False  # Variable to start main loop 

#  Position of car
car_x = 500
car_y = 500

#  Declares whether the car is going right
isRight = True
rightCount = -5 

#  Declares whether the car is going right
isLeft = True
leftCount = 5 

# Main loop
while not quit_game:  

    for event in pygame.event.get():  # Gets events from the queue
        if event.type == pygame.QUIT:  # Allows user to quit the game 
            quit_game = True  # Quits (stops) all pygame modules

    keys = pygame.key.get_pressed()  # Variable for pressing keys

    if not(isRight):  # Checks the user is not going left 
        # Detects the right key being pressed
        if keys[pygame.K_RIGHT]: 
            isRight = True

    elif not(isLeft):   # Checks the user is not going left 
        # Detects the right key being pressed
        if keys[pygame.K_LEFT]

    else:

    screen.fill(White)  # Fills the screen with a colour
     
    # Draws a square(car) 
    player = pygame.draw.rect(screen, Green, [car_x, car_y, 30,30])

    clock.tick()  # Tick speed

    pygame.display.update()  # Updates code above

pygame.quit()  # Quits (stops) all pygame modules
quit()  # Quits the app