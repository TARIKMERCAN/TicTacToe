def create_board(size):
    return [[' ' for _ in range(size)] for _ in range(size)]


def print_board(board):
    size = len(board)
    horizontal_line = '-' * (size * 4 + 1)
    vertical_lines = '|'.join(['   '] * size)
    col_headers = '   ' + '   '.join(chr(ord('A') + i) for i in range(size))
    print(col_headers)
    print('  ' + horizontal_line)

    for i, row in enumerate(board):
        row_display = ' | '.join(f"{cell}" for cell in row)
        print(f"{str(i + 1).ljust(2)}| {row_display} |")
        if i < size - 1:
            print('  ' + horizontal_line)
def initialize_board(size):
    return [[' ' for _ in range(size)] for _ in range(size)]


def print_scoreboard(player1, player2, player1_score, player2_score, player_turn):
    print(f"Player1 ({player1}) - Score: {player1_score}")
    print(f"Player2 ({player2}) - Score: {player2_score}")
    print(f"{player_turn} playing...")
    print()
def check_line(line, player_symbol):
    return all(x == player_symbol for x in line)

def check_win(board, player_symbol, required_to_win=3):
    size = len(board)
    for r in range(size):
        for c in range(size):
            if c + required_to_win <= size:  # Check row
                if check_line([board[r][i] for i in range(c, c + required_to_win)], player_symbol):
                    return True
            if r + required_to_win <= size:  # Check column
                if check_line([board[i][c] for i in range(r, r + required_to_win)], player_symbol):
                    return True
            if r + required_to_win <= size and c + required_to_win <= size:  # Check \ diagonal
                if check_line([board[i][i+c-r] for i in range(r, r + required_to_win)], player_symbol):
                    return True
            if r + required_to_win <= size and c - required_to_win >= -1:  # Check / diagonal
                if check_line([board[i][c-(i-r)] for i in range(r, r + required_to_win)], player_symbol):
                    return True
    return False

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
    choice = input("Enter 2 for a two-player game or 4 for a four-player game: ")
    if choice == '2':
        size = 5
        players = ['X', 'O']
        required_to_win = 3
    elif choice == '4':
        size = 25
        players = ['X', 'O', '#', '@']
        required_to_win = 5
    else:
        print("Invalid choice.")
        return

    board = [[' ' for _ in range(size)] for _ in range(size)]
    turn = 0
    while True:
        print_board(board)
        get_move(board, players[turn])
        if check_win(board, players[turn], required_to_win):
            print_board(board)
            print(f"Player {players[turn]} wins!")
            break
        if all(board[i][j] != ' ' for i in range(size) for j in range(size)):
            print("It's a draw!")
            break
        turn = (turn + 1) % len(players)

if __name__ == "__main__":
    main()