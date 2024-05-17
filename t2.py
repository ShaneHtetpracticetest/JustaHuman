import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Pygame Example")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Prevent the player from going out of bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600

# Create a player instance
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of all keyboard buttons
    keys = pygame.key.get_pressed()
    
    # Update the player sprite with the current key state
    all_sprites.update(keys)

    # Fill the screen with black
    screen.fill(BLACK)
    
    # Draw all sprites
    all_sprites.draw(screen)

    # Flip the display to update the screen
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

# Quit Pygame and the program
pygame.quit()
sys.exit()
