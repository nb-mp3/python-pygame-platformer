import pygame
import sys
from player import Player
from weapon import Weapon
from bullet import Bullet

pygame.init()

# === SETTINGS ===
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Create the window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Player / Weapon Test")
clock = pygame.time.Clock()

# Groups
all_sprites = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

# Player and weapon setup
player = Player(100, 500)
weapon = Weapon(player)
all_sprites.add(player)

# === MAIN LOOP ===
running = True
while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Jump
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
            elif event.key == pygame.K_x:
                weapon.shoot(bullet_group)

            # Switch weapons
            elif event.key == pygame.K_1:
                weapon.switch_weapon("rifle")
            elif event.key == pygame.K_2:
                weapon.switch_weapon("shell")
            elif event.key == pygame.K_3:
                weapon.switch_weapon("ion")

    # Update
    player.update(keys)
    bullet_group.update()

    # Draw
    screen.fill((30, 30, 30))  # Dark background
    player.draw(screen)
    weapon.draw(screen)
    bullet_group.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()