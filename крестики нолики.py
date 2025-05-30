import random

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_win(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]) or \
           all(board[j][i] == player for j in range(3)):
            return True
    return board[0][0] == board[1][1] == board[2][2] == player or \
           board[0][2] == board[1][1] == board[2][0] == player

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_ai_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Добро пожаловать в игру Крестики-Нолики против компьютера!")
    print("Ты играешь за X, компьютер — за O.")
    print("Введите координаты хода от 1 до 3 (например: 2 3)")
    print_board(board)

    while True:
        # Ход игрока
        try:
            move = input("Твой ход (строка и столбец 1–3): ")
            row, col = map(int, move.strip().split())
            if not (1 <= row <= 3 and 1 <= col <= 3):
                print("Введите значения от 1 до 3.")
                continue
            row -= 1
            col -= 1
            if board[row][col] != " ":
                print("Клетка уже занята. Попробуй снова.")
                continue
            board[row][col] = "X"
            print_board(board)

            if check_win(board, "X"):
                print("Ты победил!")
                break
            if is_draw(board):
                print("Ничья!")
                break

            # Ход компьютера
            print("Ход компьютера...")
            ai_row, ai_col = get_ai_move(board)
            board[ai_row][ai_col] = "O"
            print_board(board)

            if check_win(board, "O"):
                print("Компьютер победил!")
                break
            if is_draw(board):
                print("Ничья!")
                break
        except (ValueError, IndexError):
            print("Неверный ввод. Введите две цифры от 1 до 3 через пробел.")

if __name__ == "__main__":
    play_game()