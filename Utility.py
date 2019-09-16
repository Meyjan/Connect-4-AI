# Creating utility methods to help both AI and GUI

MAX_ROW = 6
MAX_COLUMN = 7
BLACK = 1
WHITE = 2

def checkValidInput(column):
    return (column >= 0 and column < 7)


def checkValidPosition(board, column):
    return (checkValidInput(column) and board[column - 1 + MAX_COLUMN * (MAX_ROW - 1)] == 0)


def getOpenRowInColumn(board, column):
    if (not checkValidPosition(board, column)):
        return -1
    for i in range(MAX_ROW):
        if (board[column - 1 + MAX_COLUMN * i] == 0):
            return (i + 1)

def checkWin(board, lastIdx, side):
    row = lastIdx % MAX_COLUMN
    col = lastIdx % MAX_ROW
    # Check horizontal
    for i in range(MAX_COLUMN - 3):
        for j in range(MAX_ROW):
            if board[j * MAX_COLUMN + i] == side and board[j * MAX_COLUMN + (i+1)] == side and board[j * MAX_COLUMN + (i+2)] == side and board[j * MAX_COLUMN + (i+3)] == side:
                return True

    # Check vertical
    for i in range(MAX_COLUMN):
        for j in range(MAX_ROW - 3):
            if board[j * MAX_COLUMN + i] == side and board[(j+1) * MAX_COLUMN + i] == side and board[(j+2) * MAX_COLUMN + i] == side and board[(j+3) * MAX_COLUMN + i] == side:
                return True

    # Check positive diagonal
    for i in range(MAX_COLUMN - 3):
        for j in range(MAX_ROW - 3):
            if board[j * MAX_COLUMN + i] == side and board[(j+1) * MAX_COLUMN + (i+1)] == side and board[(j+2) * MAX_COLUMN + (i+2)] == side and board[(j+3) * MAX_COLUMN + (i+3)] == side:
                return True

    # Check negative diagonal
    for i in range(MAX_COLUMN - 3):
        for j in range(3, MAX_ROW):
            if board[j * MAX_COLUMN + i] == side and board[(j-1) * MAX_COLUMN + (i+1)] == side and board[(j-2) * MAX_COLUMN + (i+2)] == side and board[(j-3) * MAX_COLUMN + (i+3)] == side:
                return True
