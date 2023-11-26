import pygame
import sys
import subprocess
import time

pygame.init()

WIDTH, HEIGHT = 600,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Start Menu")

# Load background image
background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.Font(None, 36)

def start_menu():
    while True:
        screen.blit(background_image, (0, 0))

        # Display title
        title_text = font.render("Game Start Menu", True, WHITE)
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        screen.blit(title_text, title_rect)

        # Display start button
        start_button = pygame.Rect(WIDTH // 3, HEIGHT // 2, WIDTH // 3, 50)
        pygame.draw.rect(screen, BLACK, start_button)
        start_text = font.render("Start Game", True, WHITE)
        start_text_rect = start_text.get_rect(center=start_button.center)
        screen.blit(start_text, start_text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if start_button.collidepoint(event.pos):
                    subprocess.run(["python", "Tictactoe.py"])  # Run Tictactoe.py
                    time.sleep(2)  # Add a delay (in seconds)
                    return  # Exit the start menu

# Main program
start_menu()


