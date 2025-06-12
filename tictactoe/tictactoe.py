"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    if x_count > o_count:
        return O  # O's turn
    return X  # X's turn

def actions(board):
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:  # empty spot
                possible_actions.add((i, j))
    return possible_actions

def result(board, action):
    i, j = action
    new_board = [row[:] for row in board]  # Deep copy of the board
    current_player = player(board)  # Get current player
    if new_board[i][j] is None:  # Make the move only if the cell is empty
        new_board[i][j] = current_player
        return new_board
    raise ValueError("Invalid action: cell is not empty")


def winner(board):
    # Check rows, columns, and diagonals
    lines = [
        board[0], board[1], board[2],  # rows
        [board[0][0], board[1][0], board[2][0]],  # column 0
        [board[0][1], board[1][1], board[2][1]],  # column 1
        [board[0][2], board[1][2], board[2][2]],  # column 2
        [board[0][0], board[1][1], board[2][2]],  # diagonal 1
        [board[0][2], board[1][1], board[2][0]]   # diagonal 2
    ]
    for line in lines:
        if line == [X, X, X]:
            return X
        if line == [O, O, O]:
            return O
    return None


def terminal(board):
    return winner(board) is not None or all(cell is not None for row in board for cell in row)

def utility(board):
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    return 0

def minimax(board):
    if terminal(board):
        return None  # No valid move if the game is over
    
    current_player = player(board)
    if current_player == X:
        # Maximize for X
        best_value = -math.inf
        best_move = None
        for action in actions(board):
            new_board = result(board, action)
            value = minimax_value(new_board)
            if value > best_value:
                best_value = value
                best_move = action
        return best_move
    else:
        # Minimize for O
        best_value = math.inf
        best_move = None
        for action in actions(board):
            new_board = result(board, action)
            value = minimax_value(new_board)
            if value < best_value:
                best_value = value
                best_move = action
        return best_move

def minimax_value(board):
    if terminal(board):
        return utility(board)
    current_player = player(board)
    if current_player == X:
        best_value = -math.inf
        for action in actions(board):
            new_board = result(board, action)
            value = minimax_value(new_board)
            best_value = max(best_value, value)
        return best_value
    else:
        best_value = math.inf
        for action in actions(board):
            new_board = result(board, action)
            value = minimax_value(new_board)
            best_value = min(best_value, value)
        return best_value




# def player(board):
#     """
#     Returns player who has the next turn on a board.
#     """
#     raise NotImplementedError


# def actions(board):
#     """
#     Returns set of all possible actions (i, j) available on the board.
#     """
#     raise NotImplementedError


# def result(board, action):
#     """
#     Returns the board that results from making move (i, j) on the board.
#     """
#     raise NotImplementedError


# def winner(board):
#     """
#     Returns the winner of the game, if there is one.
#     """
#     raise NotImplementedError


# def terminal(board):
#     """
#     Returns True if game is over, False otherwise.
#     """
#     raise NotImplementedError


# def utility(board):
#     """
#     Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
#     """
#     raise NotImplementedError


# def minimax(board):
#     """
#     Returns the optimal action for the current player on the board.
#     """
#     raise NotImplementedError



