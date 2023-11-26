# Tictactoe.py

import pygame
import sys
from Endgame import show_result

X = "X"
O = "O"
EMPTY = None
PLAYER = "player"
COMPUTER = "computer"

BOARD_SIZE = 3
CELL_SIZE = 200
BOARD_WIDTH = BOARD_SIZE * CELL_SIZE
BOARD_HEIGHT = BOARD_SIZE * CELL_SIZE

WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
PLAYER_COLOR = (0, 0, 255)
COMPUTER_COLOR = (255, 0, 0)

# Tạo bảng chơi
board = [[EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]

# Khởi tạo pygame
pygame.init()
WINDOW_SIZE = (BOARD_WIDTH, BOARD_HEIGHT)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tic-Tac-Toe")

game_over = False
result = None
player_turn = True

check_game = True
run = True

def draw_board():
    for row in range(1, BOARD_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, row * CELL_SIZE), (BOARD_WIDTH, row * CELL_SIZE), 5) #ngang
        pygame.draw.line(screen, LINE_COLOR, (row * CELL_SIZE, 0), (row * CELL_SIZE, BOARD_HEIGHT), 5) #dọc

# Hàm vẽ X hoặc O
def draw_xo(row, col, player):
    x = col * CELL_SIZE + CELL_SIZE // 2
    y = row * CELL_SIZE + CELL_SIZE // 2

    if player == PLAYER:
        pygame.draw.circle(screen, PLAYER_COLOR, (x, y), CELL_SIZE // 3, 3)
    else:
        pygame.draw.line(screen, COMPUTER_COLOR, (x - CELL_SIZE // 3, y - CELL_SIZE // 3), (x + CELL_SIZE // 3, y + CELL_SIZE // 3), 3)
        pygame.draw.line(screen, COMPUTER_COLOR, (x - CELL_SIZE // 3, y + CELL_SIZE // 3), (x + CELL_SIZE // 3, y - CELL_SIZE // 3), 3)

def check_winner(board, player):
    # Kiểm tra hàng và cột
    for i in range(BOARD_SIZE):
        if all(board[i][j] == player for j in range(BOARD_SIZE)):
            return True
        if all(board[j][i] == player for j in range(BOARD_SIZE)):
            return True
    # Kiểm tra đường chéo      trái trên, phải dưới                        phải trên,trái dưới
        if all(board[i][i] == player for i in range(BOARD_SIZE)) or all(board[i][2 - i] == player for i in range(BOARD_SIZE)):
            return True
    return False

# Hàm kiểm tra hòa
def check_tie(board):
    return all(board[i][j] is not None for i in range(BOARD_SIZE) for j in range(BOARD_SIZE))

# Hàm đánh giá điểm số
def evaluate(board):
    if check_winner(board, COMPUTER):
        return 1
    elif check_winner(board, PLAYER):
        return -1
    elif check_tie(board):
        return 0
    else:
        return None

# Hàm Minimax
def minimax(board, depth, is_maximizing):
    result = evaluate(board)

    if result is not None:
        return result

    if is_maximizing:
        max_eval = -float("inf")
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == EMPTY:   #Duyệt qua từng ô trống
                    board[i][j] = COMPUTER   # Thử đặt máy tính vào ô

                    # đệ quy hàm minimax với is_maximizing là False và tăng depth lên 1
                    eval = minimax(board, depth + 1, False)

                    #Sau khi đệ quy hoàn tất, đặt lại giá trị của ô về trống
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
        return max_eval
    else:           #false
        min_eval = float("inf")
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
        return min_eval

# Hàm tìm nước đi tốt nhất cho máy tính
def find_best_move(board):
    best_eval = -float("inf")
    best_move = None

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == EMPTY:
                board[i][j] = COMPUTER

                # đánh giá trạng thái sau nước đi hiện tại 'False' cho biết đang tối thiểu hóa
                eval = minimax(board, 0, False)

                board[i][j] = EMPTY
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)

    return best_move
def reset_game():
    global game_over, result, player_turn, board

    game_over = False
    result = None
    player_turn = True
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]

# Vòng lặp chính
def start_game():
    global game_over, result, player_turn, board

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if player_turn:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    col = event.pos[0] // CELL_SIZE
                    row = event.pos[1] // CELL_SIZE
                    if board[row][col] == EMPTY:
                        board[row][col] = PLAYER
                        player_turn = False

            if not player_turn and not game_over:
                move = find_best_move(board)
                if move:
                    board[move[0]][move[1]] = COMPUTER
                    player_turn = True

            result = evaluate(board)
            if result is not None:
                game_over = True

        screen.fill(WHITE)
        draw_board()

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if board[row][col] == PLAYER:
                    draw_xo(row, col, PLAYER)
                elif board[row][col] == COMPUTER:
                    draw_xo(row, col, COMPUTER)

        pygame.display.flip()  # hiển thị trạng thái mới của trò chơi lên màn hình

    result_text = None
    if result == 1:
        result_text = "Computer Win!"
    elif result == -1:
        result_text = "Player Win!"
    else:
        result_text = "Drawn!"

    print(result_text)

    show_result(result_text)

if __name__ == "__main__":
    start_game()
