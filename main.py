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

def main():
    board_size = int(input("Enter the size of the board: "))
    board = create_board(board_size)
    print_board(board)

if __name__ == "__main__":
    main()
