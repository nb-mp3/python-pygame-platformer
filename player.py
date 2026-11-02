import pygame
import os
from beam import UniBeam

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # === ANIMATION SETTINGS ===
        self.frame_width = 48
        self.frame_height = 48
        self.frame_rate = 100  # milliseconds between frames

        # === PLAYER STATES ===
        self.animations = {
            "idle": self.load_animation("Cyborg_idle.png"),
            "run": self.load_animation("Cyborg_run.png"),
            "jump": self.load_animation("Cyborg_jump.png"),
            "doublejump": self.load_animation("Cyborg_doublejump.png"),
            "attack": self.load_animation("Cyborg_attack1.png"),
            "climb": self.load_animation("Cyborg_climb.png"),
            "hurt": self.load_animation("Cyborg_hurt.png"),
            "death": self.load_animation("Cyborg_death.png"),
        }

        self.state = "idle"
        self.frames = self.animations[self.state]
        self.current_frame = 0
        self.animation_timer = 0

        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(topleft=(x, y))

        # === MOVEMENT ===
        self.speed = 5
        self.jump_speed = -10
        self.velocity_y = 0
        self.gravity = 0.5
        self.on_ground = False
        self.facing_direction = 1  # 1 = right, -1 = left

        # === DOUBLE JUMP ===
        self.jump_count = 0
        self.max_jumps = 2

    def load_animation(self, filename):
        path = os.path.join("assets", "player", filename)
        sheet = pygame.image.load(path).convert_alpha()
        frames = []
        for x in range(0, sheet.get_width(), self.frame_width):
            frame = sheet.subsurface(pygame.Rect(x, 0, self.frame_width, self.frame_height))
            frames.append(frame)
        return frames

    def change_state(self, new_state):
        if self.state != new_state:
            self.state = new_state
            self.frames = self.animations[self.state]
            self.current_frame = 0
            self.animation_timer = pygame.time.get_ticks()
            self.image = self.frames[self.current_frame]

    def update_animation(self):
        now = pygame.time.get_ticks()
        if now - self.animation_timer > self.frame_rate:
            self.animation_timer = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            if self.facing_direction == -1:
                self.image = pygame.transform.flip(self.frames[self.current_frame], True, False)

    def update(self, keys_pressed):
        moving = False

        # === HORIZONTAL MOVEMENT ===
        if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed
            moving = True
            self.facing_direction = -1
        if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speed
            moving = True
            self.facing_direction = 1

        # === GRAVITY ===
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # === FLOOR COLLISION ===
        if self.rect.bottom >= 600:
            self.rect.bottom = 600
            self.velocity_y = 0
            self.on_ground = True
            self.jump_count = 0
        else:
            self.on_ground = False

        # === STATE ===
        if not self.on_ground:
            if self.jump_count == 2:
                self.change_state("doublejump")
            else:
                self.change_state("jump")
        elif moving:
            self.change_state("run")
        else:
            self.change_state("idle")

        self.update_animation()

    def jump(self):
        if self.jump_count < self.max_jumps:
            self.velocity_y = self.jump_speed
            self.jump_count += 1
            if self.jump_count == 2:
                self.change_state("doublejump")
            else:
                self.change_state("jump")

    def shoot_unibeam(self, beam_group):
        chest_x = self.rect.centerx
        chest_y = self.rect.centery - 10
        beam = UniBeam(chest_x, chest_y, self.facing_direction)
        beam_group.add(beam)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
