import math

# Creating utility methods to help both AI and GUI

MAX_ROW = 6
MAX_COLUMN = 7
BLACK = 1
WHITE = 2

def getArrayIndex(row, col):
    return ((row - 1) * MAX_COLUMN + col - 1)

def checkValidInput(column):
    return (column > 0 and column < MAX_COLUMN + 1)


def checkValidPosition(board, column):
    return (checkValidInput(column) and board[column - 1 + MAX_COLUMN * (MAX_ROW - 1)] == 0)


def getOpenRowInColumn(board, column):
    if (not checkValidPosition(board, column)):
        return -1
    for i in range(MAX_ROW):
        if (board[column - 1 + MAX_COLUMN * i] == 0):
            return (i + 1)

def fill(board, number, side):
    i = number - 1
    while i < len(board):
        if(board[i] == 0):
            board[i] = side
            break
        else:
            i += 7
    return i

def printBoard(board):
    init = MAX_ROW * MAX_COLUMN - MAX_COLUMN
    for i in range(len(board)):
        print(board[init+i], end = ' ')
        if(i % MAX_COLUMN == MAX_COLUMN-1):
            print()
            init = init - (MAX_COLUMN * 2)

def checkWin(board, lastIdx, side):
    row = math.floor(lastIdx / MAX_COLUMN)
    col = lastIdx - (row * MAX_COLUMN)
    # Check horizontal
    for i in range(MAX_ROW):
        if (not (i == row)):
            continue
        for j in range(math.ceil(MAX_COLUMN / 2)):
            if board[i * MAX_COLUMN + j] == side and board[i * MAX_COLUMN + (j+1)] == side and board[i * MAX_COLUMN + (j+2)] == side and board[i * MAX_COLUMN + (j+3)] == side:
                return True

    # Check vertical
    for i in range(MAX_COLUMN):
        if (not (i == col)):
            continue
        for j in range(math.ceil(MAX_ROW / 2)):
            if board[j * MAX_COLUMN + i] == side and board[(j+1) * MAX_COLUMN + i] == side and board[(j+2) * MAX_COLUMN + i] == side and board[(j+3) * MAX_COLUMN + i] == side:
                return True

    # Check positive diagonal
    for i in range(math.ceil(MAX_COLUMN / 2)):
        for j in range(math.ceil(MAX_ROW / 2)):
            if (lastIdx not in ((j * MAX_COLUMN + i), ((j+1) * MAX_COLUMN + (i+1)), ((j+2) * MAX_COLUMN + (i+2)), ((j+3) * MAX_COLUMN + (i+3)))):
                continue
            if board[j * MAX_COLUMN + i] == side and board[(j+1) * MAX_COLUMN + (i+1)] == side and board[(j+2) * MAX_COLUMN + (i+2)] == side and board[(j+3) * MAX_COLUMN + (i+3)] == side:
                return True

    # Check negative diagonal
    for i in range(math.ceil(MAX_COLUMN / 2)):
        for j in range(math.ceil(MAX_ROW/2), MAX_ROW):
            if (lastIdx not in ((j * MAX_COLUMN + i), ((j-1) * MAX_COLUMN + (i+1)), ((j-2) * MAX_COLUMN + (i+2)), ((j-3) * MAX_COLUMN + (i+3)))):
                continue
            if board[j * MAX_COLUMN + i] == side and board[(j-1) * MAX_COLUMN + (i+1)] == side and board[(j-2) * MAX_COLUMN + (i+2)] == side and board[(j-3) * MAX_COLUMN + (i+3)] == side:
                return True
