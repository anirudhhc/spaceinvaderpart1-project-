import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Player vs Enemies")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player settings
player_size = 50
player_pos = [screen_width // 2, screen_height // 2]
player_speed = 5

# Enemy settings
enemy_size = 50
enemy_count = 7
enemies = []
for _ in range(enemy_count):
    x_pos = random.randint(0, screen_width - enemy_size)
    y_pos = random.randint(0, screen_height - enemy_size)
    enemies.append(pygame.Rect(x_pos, y_pos, enemy_size, enemy_size))

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < screen_width - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < screen_height - player_size:
        player_pos[1] += player_speed

    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    pygame.draw.rect(screen, BLUE, player_rect)

    # Enemy handling
    for enemy_rect in enemies:
        pygame.draw.rect(screen, RED, enemy_rect)

        # Collision detection
        if player_rect.colliderect(enemy_rect):
            score += 1
            # Respawn enemy in random position
            enemy_rect.x = random.randint(0, screen_width - enemy_size)
            enemy_rect.y = random.randint(0, screen_height - enemy_size)

    # Display score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
