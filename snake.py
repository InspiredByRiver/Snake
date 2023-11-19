import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set the size of the game window
window_width=800
window_height=600
game_window = pygame.display.set_mode((window_width,window_height))

# Define Colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake Properties
snake.pos = [[100,50]]
snake_size = 20
dx = snake_size
dy = 0

# Food properties
food_pos = [random.randrange(1, (window_width//snake_size)) * snake_size,
            random.randrange(1, (window_height//snake_size)) * snake_size]
food_size = 20

# Game loop control 
clock = pygame.time.Clock()
running = True

# Main Game Loop
while running:
    # Handling Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy != snake_size:
                dx, dy = 0, -snake_size
            elif event.key == pygame.K_DOWN and dy != -snake_size:
                dx, dy = 0, snake_size
            elif event.key == pygame.K_LEFT and dx != snake_size:
                dx, dy = -snake_size, 0
            elif event.key == pygame.K_RIGHT and dx != -snake_size:
                dx, dy = snake_size, 0

