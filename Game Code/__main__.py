# === IMPORTS === #

import pygame   # Core library for game development
import sys  # For system-level functions like exiting the program
import os   # For handling file paths

# Import settings and utility functions/constants from another module (settings.py)

from settings import (
    SCREEN_WIDTH, SCREEN_HEIGHT, FPS,
    BLACK, WHITE, GRAY, BRIGHT_GREEN, AQUA,
    CUSTOM_COLOR_1, CUSTOM_COLOR_2, CUSTOM_COLOR_3,
    get_font, text_objects, button
)

from player import Player

# Create player instance
player = Player(100, 500)
player_group = pygame.sprite.Group()
player_group.add(player)




# === INITIALISE PYGAME === #

pygame.init()   # Sets up all the modules in Pygame

# === SETUP DISPLAY AND CLOCK === #

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Create the game window
pygame.display.set_caption("Cyber Tower Escape") # Set the window title
clock = pygame.time.Clock() # Clock object to control the frame rate

# === BACKGROUND LOADER FUNCTION === #

def load_backgrounds():
    # Internal helper to load and scale background images
    def load(path):
        img = pygame.image.load(path).convert() # Load image and convert for faster blitting
        return pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)) # Resize to fit screen

    # Return dictionary containing all background images
    return {
        "menu": load("assets/backgrounds/menu_bg.png"),
        "game": load("assets/backgrounds/menu_bg(1).png"),
        "scoreboard": load("assets/backgrounds/menu_bg(2).png"),
        "howtoplay": load("assets/backgrounds/menu_bg(3).png")
    }

# Load all backgrounds into a dictionary
backgrounds = load_backgrounds()

# === MAIN MENU FUNCTION === #
def main_menu():
    while True:
          # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        # Draw background for menu
        screen.blit(backgrounds["menu"], (0, 0))

        # Title text
        title_font = get_font(50)
        title_surf, title_rect = text_objects("CYBER TOWER ESCAPE", title_font)
        title_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 5)
        screen.blit(title_surf, title_rect)

        # Menu Buttons
        button("Start Game", 325, 250, 150, 50, BLACK, CUSTOM_COLOR_1, game_loop, screen)
        button("Scoreboard", 325, 325, 150, 50, BLACK, CUSTOM_COLOR_2, score_board, screen)
        button("How To Play", 325, 400, 150, 50, BLACK, CUSTOM_COLOR_3, how_to_play, screen)

        # Update display and control frame rate
        pygame.display.update()
        clock.tick(FPS)

# === GAMEPLAY SCREEN === #
def game_loop():
    running = True
    while running:
         # Handle quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        screen.blit(backgrounds["game"], (0, 0))

        # Gameplay text
        text, rect = text_objects("Game Playing...", get_font(40))
        rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
        screen.blit(text, rect)
        
        keys = pygame.key.get_pressed()
        player.update(keys)
        player_group.draw(screen)


        # Gameplay Buttons
        button("Main Menu", 150, 500, 120, 40, GRAY, BRIGHT_GREEN, main_menu, screen)
        button("Scoreboard", 340, 500, 120, 40, GRAY, BRIGHT_GREEN, score_board, screen)
        button("How To Play", 530, 500, 120, 40, GRAY, BRIGHT_GREEN, how_to_play, screen)

        pygame.display.update()
        clock.tick(FPS)

# === SCOREBOARD SCREEN === #
def score_board():
    viewing = True
    while viewing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        screen.blit(backgrounds["scoreboard"], (0, 0))

        # Scoreboard text
        text, rect = text_objects("SCOREBOARD", get_font(40))
        rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 5)
        screen.blit(text, rect)

        # Scoreboard Buttons
        button("Main Menu", 150, 500, 120, 40, GRAY, BRIGHT_GREEN, main_menu, screen)
        button("Start Game", 340, 500, 120, 40, GRAY, BRIGHT_GREEN, game_loop, screen)
        button("How To Play", 530, 500, 120, 40, GRAY, BRIGHT_GREEN, how_to_play, screen)

        pygame.display.update()
        clock.tick(FPS)

# === HOW TO PLAY SCREEN === #
def how_to_play():
    viewing = True
    while viewing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        screen.blit(backgrounds["howtoplay"], (0, 0))

        # How to Play text
        text, rect = text_objects("HOW TO PLAY", get_font(40))
        rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 5)
        screen.blit(text, rect)

        # Instructions
        instructions = [
            "W / ↑ = Climb ladder",
            "A / ← = Move left",
            "D / → = Move right",
            "Space = Jump",
            "X = Shoot"
        ]

        for i, line in enumerate(instructions):
            instr_text, instr_rect = text_objects(line, get_font(24))
            instr_rect.center = (SCREEN_WIDTH / 2, 200 + i * 40)
            screen.blit(instr_text, instr_rect)

        button("Main Menu", 325, 500, 150, 50, GRAY, BRIGHT_GREEN, main_menu, screen)

        pygame.display.update()
        clock.tick(FPS)

# === QUIT FUNCTION === #
def quit_game():
    pygame.quit()
    sys.exit()

# === START THE GAME === #
main_menu()  # Launches the main menu when the script starts
