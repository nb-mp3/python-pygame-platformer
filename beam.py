import pygame
import os

class UniBeam(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.speed = 15
        self.direction = direction

        # Load ion blaster bullet image
        self.image = pygame.image.load(
            os.path.join("assets", "bullets", "ion_ammo.png")
        ).convert_alpha()

        # Scale image to a reasonable size
        self.image = pygame.transform.scale(self.image, (20, 10))

        # Flip image if going left
        if self.direction == -1:
            self.image = pygame.transform.flip(self.image, True, False)

        # Start position from chest area
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.x += self.speed * self.direction

        # Remove projectile if it leaves the screen
        if self.rect.right < 0 or self.rect.left > 800:
            self.kill()
