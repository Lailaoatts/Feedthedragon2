import pygame

# start pygame modules
pygame.init()

# Set the display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption      ("Feed the dragon")

FPS= 60
clock=pygame.time.Clock()


# The main game loop
''' 5 CONSTANTS
PLAYER_STARTING_LIVES,5
PLAYER_VELOCITY, 10
COIN_STARTING_VELOCITY, 10
COIN_ACCELERATION, 0.5
BUFFER_DISTANCE,100
'''
PLAYER_STARTING_LIVES = 5
''' 3 variables
player_lives,player_starting

















running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
