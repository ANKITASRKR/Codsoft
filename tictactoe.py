import math

# Tic-Tac-Toe Board
board = [' ' for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def check_winner(board):
    # Winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != ' ':
            return board[combo[0]]
    
    return None

def is_board_full(board):
    return ' ' not in board

def minimax(board, depth, is_maximizing, alpha, beta):
    scores = {'X': 1, 'O': -1, 'tie': 0}
    result = check_winner(board)
    
    if result != None:
        return scores[result]
    
    if is_board_full(board):
        return scores['tie']
    
    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def best_move(board):
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            move_val = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

def human_move():
    move = int(input("Enter your move (1-9): ")) - 1
    while board[move] != ' ':
        move = int(input("Invalid move! Enter your move (1-9): ")) - 1
    return move

def play_game():
    while True:
        print_board()
        if is_board_full(board) or check_winner(board):
            break

        if check_winner(board):
            print(f"{check_winner(board)} wins!")
            break

        if board.count(' ') % 2 == 0:  # AI's turn
            move = best_move(board)
            board[move] = 'X'
        else:  # Human's turn
            move = human_move()
            board[move] = 'O'

    if not check_winner(board):
        print("It's a tie!")
    else:
        print(f"{check_winner(board)} wins!")
    print_board()

if __name__ == "__main__":
    play_game()
