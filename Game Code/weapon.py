import pygame
import os
from bullet import Bullet

class Weapon:
    def __init__(self, owner):
        self.owner = owner
        self.bullet_type = "rifle"
        self.image = self.load_image("Rifle_1.png", (18, 5))
        self.cooldown = 300
        self.last_shot = 0

        # Offsets: (right_x, right_y, left_x, left_y, barrel_offset)
        self.weapon_offsets = {
            "rifle": (10, 5, -28, 5, 16),
            "shell": (12, 6, -30, 6, 14),
            "ion":   (11, 6, -28, 6, 14),
        }

        self.right_x, self.right_y, self.left_x, self.left_y, self.barrel_offset = self.weapon_offsets["rifle"]

        # Debug mode toggle
        self.debug_mode = True

    def load_image(self, filename, size=None):
        img = pygame.image.load(os.path.join("assets", "weapons", filename)).convert_alpha()
        if size:
            img = pygame.transform.scale(img, size)
        return img

    def switch_weapon(self, new_type):
        self.bullet_type = new_type

        if new_type == "rifle":
            self.image = self.load_image("Rifle_1.png", (18, 5))
        elif new_type == "shell":
            self.image = self.load_image("shellshooter.png", (20, 10))
        elif new_type == "ion":
            self.image = self.load_image("ionblaster.png", (18, 10))

        self.right_x, self.right_y, self.left_x, self.left_y, self.barrel_offset = self.weapon_offsets[new_type]

    def shoot(self, bullet_group):
        now = pygame.time.get_ticks()
        if now - self.last_shot >= self.cooldown:
            if self.owner.facing_right:
                bullet_x = self.owner.rect.centerx + self.barrel_offset
                direction = 1
            else:
                bullet_x = self.owner.rect.centerx - self.barrel_offset
                direction = -1

            bullet_y = self.owner.rect.centery + self.right_y
            bullet = Bullet(bullet_x, bullet_y, direction=direction, bullet_type=self.bullet_type)
            bullet_group.add(bullet)
            self.last_shot = now

    def draw(self, screen):
        # Draw the weapon
        if self.owner.facing_right:
            weapon_rect = self.image.get_rect(topleft=(self.owner.rect.centerx + self.right_x,
                                                       self.owner.rect.centery + self.right_y))
            screen.blit(self.image, weapon_rect.topleft)
        else:
            flipped_img = pygame.transform.flip(self.image, True, False)
            weapon_rect = flipped_img.get_rect(topleft=(self.owner.rect.centerx + self.left_x,
                                                        self.owner.rect.centery + self.left_y))
            screen.blit(flipped_img, weapon_rect.topleft)

       
