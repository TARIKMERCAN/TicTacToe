def create_board(size):
    return [[' ' for _ in range(size)] for _ in range(size)]


def print_board(board):
    size = len(board)
    horizontal_line = '-' * (size * 4 + 1)
    vertical_lines = '|'.join([' '] * size)
    col_headers = ' ' + ' '.join(chr(ord('A') + i) for i in range(size))
    print(col_headers)
    print(' ' + horizontal_line)
    for i, row in enumerate(board):
        row_display = ' | '.join(f"{cell}" for cell in row)
        print(f"{str(i + 1).ljust(2)}| {row_display} |")
        if i < size - 1:
            print(' ' + horizontal_line)


def initialize_board(size):
    return [[' ' for _ in range(size)] for _ in range(size)]


def get_move(board, player_symbol):
    size = len(board)
    while True:
        move = input(f"Player {player_symbol}, enter your move (e.g., a1): ").lower()
        if len(move) >= 2 and move[0].isalpha() and move[1:].isdigit():
            col = ord(move[0]) - ord('a')
            row = int(move[1:]) - 1  # This change allows for double-digit numbers.
            if 0 <= row < size and 0 <= col < size and board[row][col] == ' ':
                board[row][col] = player_symbol
                return
        print("Invalid move, try again.")


def main():
    board_size = int(input("Enter the size of the board: "))
    board = create_board(board_size)
    print_board(board)


if __name__ == "__main__":
    main()