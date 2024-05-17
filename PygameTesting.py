import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Example")

# Set up colors
RED = (255, 0, 0)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    window.fill((0, 0, 0))

    # Draw a red rectangle
    pygame.draw.rect(window, RED, (300, 200, 200, 100))

    # Update the display
    pygame.display.update()
