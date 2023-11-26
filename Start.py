# StartGame.py

import pygame
import sys
import subprocess
import TicTacToe

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Start Menu")

background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 36)

def start_menu():
    check_game = True  # Biến kiểm tra xem trò chơi đã kết thúc chưa
    run = True

    while run:
        screen.blit(background_image, (0, 0))

        title_text = font.render("Game Start Menu", True, WHITE)
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        screen.blit(title_text, title_rect)

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
                    check_game = TicTacToe.start_game()

# Main program
start_menu()
