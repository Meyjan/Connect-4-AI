# Creating utility methods to help both AI and GUI

ROW_COUNT = 6
COLUMN_COUNT = 7


def checkValidInput(column):
    return (column >= 0 and column < 7)


def checkValidPosition(board, column):
    return (checkValidInput(column) and board[column - 1 + COLUMN_COUNT * (ROW_COUNT - 1)] == 0)


def getOpenRowInColumn(board, column):
    if (not checkValidPosition(board, column)):
        return -1
    for i in range(ROW_COUNT):
        if (board[column - 1 + COLUMN_COUNT * i] == 0):
            return (i + 1)
