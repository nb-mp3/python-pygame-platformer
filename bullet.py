import pygame
import os

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, bullet_type):
        super().__init__()
        self.direction = direction
        self.speed = 10

        # Load different images based on type
        if bullet_type == "rifle":
            self.image = pygame.image.load(os.path.join("assets", "bullets", "rifle_ammo.png")).convert_alpha()
        elif bullet_type == "shell":
            self.image = pygame.image.load(os.path.join("assets", "bullets", "shell.png")).convert_alpha()
        elif bullet_type == "ion":
            self.image = pygame.image.load(os.path.join("assets", "bullets", "ion_ammo.png")).convert_alpha()
        else:
            self.image = pygame.Surface((10, 5))
            self.image.fill((255, 255, 255))

        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.x += self.speed * self.direction

        if self.rect.right < 0 or self.rect.left > 800:
            self.kill()
