import pygame
from player import Player
from beam import UniBeam

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("UniBeam Test")
clock = pygame.time.Clock()

# Groups
player = Player(100, 500)
player_group = pygame.sprite.Group(player)
beam_group = pygame.sprite.Group()

# Shooting control
shooting = False
shoot_cooldown = 100  # ms
last_shot_time = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                shooting = True
            elif event.key == pygame.K_SPACE:
                player.jump()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_x:
                shooting = False

    keys = pygame.key.get_pressed()
    player.update(keys)

    # Continuous shooting if holding X
    if shooting:
        now = pygame.time.get_ticks()
        if now - last_shot_time > shoot_cooldown:
            player.shoot_unibeam(beam_group)
            last_shot_time = now

    beam_group.update()

    # Draw
    screen.fill((30, 30, 30))
    player_group.draw(screen)
    beam_group.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
