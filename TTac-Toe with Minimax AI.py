import random

board = [' ' for _ in range(9)]  # Initialize the game board with empty spaces

def print_board():
    # Print the board in a readable format
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def check_win(board, player):
    # Define winning conditions (row, column, diagonal)
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    # Check if any of the win conditions are met for the given player
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    # Check if the board is full and there is no winner (draw)
    return ' ' not in board

def minimax(board, depth, is_maximizing):
    # Base cases for recursion: check for win or draw
    if check_win(board, 'X'):
        return -10
    if check_win(board, 'O'):
        return 10
    if check_draw(board):
        return 0

    if is_maximizing:
        # Maximizing player (AI) tries to get the highest score
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'  # AI makes a move
                score = minimax(board, depth + 1, False)
                board[i] = ' '  # Undo the move
                best_score = max(score, best_score)
        return best_score
    else:
        # Minimizing player (human) tries to get the lowest score
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'  # Human makes a move
                score = minimax(board, depth + 1, True)
                board[i] = ' '  # Undo the move
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    # Determine the best move for the AI using Minimax
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'  # AI makes a move
            score = minimax(board, 0, False)
            board[i] = ' '  # Undo the move
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    current_player = 'X'  # Start with the human player
    while True:
        print_board()
        if current_player == 'X':
            move = input("Player X, enter your move (1-9): ")
            move = int(move) - 1
            if board[move] == ' ':
                board[move] = 'X'  # Human makes a move
                if check_win(board, 'X'):
                    print_board()
                    print("Player X wins! Congratulations!")
                    break
                elif check_draw(board):
                    print_board()
                    print("It's a draw!")
                    break
                current_player = 'O'  # Switch to AI
            else:
                print("Invalid move, try again.")
        else:
            move = best_move(board)  # AI determines the best move
            board[move] = 'O'
            print("Player O (AI) moves to position {}".format(move + 1))
            if check_win(board, 'O'):
                print_board()
                print("Player O (AI) wins!")
                break
            elif check_draw(board):
                print_board()
                print("It's a draw!")
                break
            current_player = 'X'  # Switch to human player

if __name__ == "__main__":
    play_game()
    input("Press Enter to exit...")
