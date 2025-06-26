import pygame
import time
import random
from random import randint
pygame.init()  # Initialises (starts) all pygame modules

Width = 1000
Height = 750

v = 0

screen = pygame.display.set_mode((Width, Height))  # Creates a surface
game_icon = pygame.image.load('game_icon.png')  # Loads the icon
pygame.display.set_icon(game_icon)  # Displays the icon
pygame.display.set_caption("Race Game by Ezray")  # Displays Caption

White = (255, 255, 255)  # Colour of screen
Black = (0, 0, 0)  # Colour of track lines
Green = (0, 128, 0)  # Colour of enemy car
Red = (255, 0, 0)  # Colour of obstacle

font = pygame.font.Font("freesansbold.ttf", 50)
score_font = pygame.font.Font("freesansbold.ttf", 30) # Smaller font for score

# Car details
carX = 450
carY = 550
car_width = 50
car_height = 60
vel = 5

# Score system
score = 0
score_increase = 1 # Corrected variable name from score_incease

# Co-ordinates for obstacles
obs_width = 50
obs_height = 60

# Define possible lane X coordinates for obstacles
lane_x_positions = [350, 450, 550, 650] # Represents the center of each lane visually

# Initialize obstacles with random starting positions and speeds
# This ensures they don't all start at the same spot in the first frame
obsX1 = random.choice(lane_x_positions)
obsY1 = random.randint(-400, -100) # Stagger initial Y positions
obsY1_change = random.randint(4, 8)

obsX2 = random.choice(lane_x_positions)
# Ensure initial obstacles don't overlap too much by staggering Y
obsY2 = random.randint(-800, -500)
obsY2_change = random.randint(4, 8)

obsX3 = random.choice(lane_x_positions)
obsY3 = random.randint(-1200, -900)
obsY3_change = random.randint(4, 8)

obsX4 = random.choice(lane_x_positions)
obsY4 = random.randint(-1600, -1300)
obsY4_change = random.randint(4, 8)


def player():
    # Draws a square (car) and returns its Rect object
    return pygame.draw.rect(screen, Green, [carX, carY, car_width, car_height])

def draw_obstacle(x, y, width, height):
    # Draws a square (obstacle) and returns its Rect object
    return pygame.draw.rect(screen, Red, [x, y, width, height])

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

def display_score(current_score):
    score_text = score_font.render(f"Score: {current_score}", True, Black)
    screen.blit(score_text, (10, 10))


clock = pygame.time.Clock()  # tick speed

quit_game = False  # Variable to start main loop

# Main loop
while not quit_game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Allows user to quit the game
            quit_game = True

    keys = pygame.key.get_pressed()  # Variable for pressing keys

    # Car movement left/right
    if keys[pygame.K_LEFT] and carX > 320:
        carX -= vel
    elif keys[pygame.K_RIGHT] and carX < 670:
        carX += vel

    # Continuous speed of obstacles
    obsY1 += obsY1_change
    obsY2 += obsY2_change
    obsY3 += obsY3_change
    obsY4 += obsY4_change

    screen.fill(White)  # Fills the screen with a colour

    track()

    # Draw player and obstacles, getting their Rect objects for collision
    player_rect = player()
    obstacle_1_rect = draw_obstacle(obsX1, obsY1, obs_width, obs_height)
    obstacle_2_rect = draw_obstacle(obsX2, obsY2, obs_width, obs_height)
    obstacle_3_rect = draw_obstacle(obsX3, obsY3, obs_width, obs_height)
    obstacle_4_rect = draw_obstacle(obsX4, obsY4, obs_width, obs_height)

    # Collision with player and obstacles
    if player_rect.colliderect(obstacle_1_rect) or \
       player_rect.colliderect(obstacle_2_rect) or \
       player_rect.colliderect(obstacle_3_rect) or \
       player_rect.colliderect(obstacle_4_rect):
        quit_game = True

    # --- New: Reset obstacles and increment score when they go off-screen ---
    if obsY1 > Height:
        obsY1 = -obs_height - random.randint(0, 200) # Reset above screen, add random offset
        obsX1 = random.choice(lane_x_positions) # New random lane
        obsY1_change = random.randint(4, 8) # New random speed
        score += score_increase

    if obsY2 > Height:
        obsY2 = -obs_height - random.randint(0, 200)
        obsX2 = random.choice(lane_x_positions)
        obsY2_change = random.randint(4, 8)
        score += score_increase

    if obsY3 > Height:
        obsY3 = -obs_height - random.randint(0, 200)
        obsX3 = random.choice(lane_x_positions)
        obsY3_change = random.randint(4, 8)
        score += score_increase

    if obsY4 > Height:
        obsY4 = -obs_height - random.randint(0, 200)
        obsX4 = random.choice(lane_x_positions)
        obsY4_change = random.randint(4, 8)
        score += score_increase
    # --- End of New Reset Logic ---

    display_score(score) # Display the current score

    clock.tick(50)  # Tick speed

    pygame.display.update()  # Updates code above

message("You died!", White, Black) # Displays message
pygame.display.update()
time.sleep(2)

pygame.quit()  # Quits (stops) all pygame modules
quit()  # Quits the app