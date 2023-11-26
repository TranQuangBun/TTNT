# Endgame.py

import pygame
import sys
import subprocess

def show_result(result_text):
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Kết quả")

    # Thêm hình nền
    background = pygame.image.load("winner.png")
    background = pygame.transform.scale(background, (600, 600))

    font = pygame.font.Font(None, 36)
    text = font.render(result_text, True, (0, 0, 0))
    text_rect = text.get_rect(center=(200, 100))

    replay_button = pygame.Rect(50, 200, 150, 50)
    exit_button = pygame.Rect(200, 200, 150, 50)

    # Canh giữa các nút và chữ
    text_rect.center = (screen.get_width() // 2, 100)
    replay_button.x = (screen.get_width() - replay_button.width) // 4
    exit_button.x = 3 * (screen.get_width() - exit_button.width) // 4

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if replay_button.collidepoint(mouse_pos):
                    # Chơi lại
                    subprocess.run(["python", "TicTacToe.py"])
                    sys.exit()
                elif exit_button.collidepoint(mouse_pos):
                    # Thoát
                    sys.exit()

        # Hiển thị hình nền
        screen.blit(background, (0, 0))
        screen.blit(text, text_rect)

        pygame.draw.rect(screen, (0, 255, 0), replay_button)
        pygame.draw.rect(screen, (255, 0, 0), exit_button)

        font = pygame.font.Font(None, 30)
        replay_text = font.render("Play Again", True, (0, 0, 0))
        exit_text = font.render("Out Game", True, (0, 0, 0))

        # Canh giữa văn bản trên nút
        screen.blit(replay_text, (replay_button.x + (replay_button.width - replay_text.get_width()) // 2, replay_button.y + 15))
        screen.blit(exit_text, (exit_button.x + (exit_button.width - exit_text.get_width()) // 2, exit_button.y + 15))

        pygame.display.flip()

if __name__ == "__main__":
    result_text = sys.argv[1]
    show_result(result_text)
