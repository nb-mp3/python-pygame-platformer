import pygame
import sys

# Game settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# === COLOUR CONSTANTS ===
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (190, 190, 190)
BRIGHT_GREEN = (0, 255, 0)
AQUA = (0, 128, 128)
CUSTOM_COLOR_1 = (194, 82, 225 )  # Example custom color
CUSTOM_COLOR_2 = (88, 106, 226)  # Example custom color
CUSTOM_COLOR_3 = (42, 35, 86)  # Example custom color

# Create screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cyber Tower Escape")
clock = pygame.time.Clock()


# === FONT FUNCTION ===
def get_font(size):
    return pygame.font.SysFont("tahoma", size)

# === TEXT RENDERING ===
def text_objects(text, font):
    text_surface = font.render(text, True, WHITE)
    return text_surface, text_surface.get_rect()

# === BUTTON FUNCTION ===
def button(msg, x, y, w, h, color, hover_color, action=None, screen=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, hover_color, (x, y, w, h))
        if click[0] == 1 and action:
            pygame.time.wait(200)
            action()
    else:
        pygame.draw.rect(screen, color, (x, y, w, h))

    small_text = get_font(20)
    text_surf, text_rect = text_objects(msg, small_text)
    text_rect.center = (x + w / 2, y + h / 2)
    screen.blit(text_surf, text_rect)
