import random
import Utility as util
import copy
import math

moveAIList = []

for i in range(util.MAX_COLUMN):
    moveAIList.append(i+1)

board = [0] * 42
# board[0] = 2
# board[1] = 1
# board[2] = 1
# board[3] = 2
# board[7] = 1
# board[8] = 1
# board[9] = 2
# board[14] = 1
# board[15] = 2

# Board menggambarkan state board sekarang
# aiNumber merupakan nomor AI yang direpresentasikan oleh board
def aiMove(board, side):
    move = random.choice(moveAIList)
    while(not util.checkValidPosition(board, move)):
        move = random.choice(moveAIList)
    return move

# Menghitung jumlah langkah yang masih dapat dilakukan walaupun sudah menang
def countLastStone(board):
    remainingStones = (1 + board.count(0)) // 2
    return (remainingStones * 10000)

# Menghitung jumlah kemenangan yang mungkin dimiliki oleh user
def countWinPossibility(board, side):
    # Initiate
    totalScore = 0
    enemySide = 0
    if (side == util.WHITE):
        enemySide = util.BLACK
    else:
        enemySide = util.WHITE

    # Check potential winning condition
    # Horizontal check
    for i in range(1, util.MAX_ROW + 1):
        for j in range(1, util.MAX_COLUMN - 2):
            lowerLimit = util.getArrayIndex(i, j)
            upperLimit = util.getArrayIndex(i, j + 3)
            totalScore += scoreAssessing(board, side, enemySide, lowerLimit, upperLimit, 1)

    # Vertical check
    for i in range(1, util.MAX_COLUMN + 1):
        for j in range(1, util.MAX_ROW - 2):
            lowerLimit = util.getArrayIndex(j, i)
            upperLimit = util.getArrayIndex(j + 3, i)
            totalScore += scoreAssessing(board, side, enemySide, lowerLimit, upperLimit, 7)

    # Diagonal ascending check
    for i in range(1, util.MAX_ROW - 2):
        for j in range(1, util.MAX_COLUMN - 2):
            lowerLimit = util.getArrayIndex(i, j)
            upperLimit = util.getArrayIndex(i + 3, j + 3)
            totalScore += scoreAssessing(board, side, enemySide, lowerLimit, upperLimit, 8)

    # Diagonal descending check
    for i in range(1, util.MAX_ROW - 2):
        for j in range(4, util.MAX_COLUMN + 1):
            lowerLimit = util.getArrayIndex(i, j)
            upperLimit = util.getArrayIndex(i + 3, j - 3)
            totalScore += scoreAssessing(board, side, enemySide, lowerLimit, upperLimit, 6)

    return totalScore



def scoreAssessing(board, side, enemySide, lowLimit, upLimit, skip):
    # Counting
    meCount = 0
    enemyCount = 0
    for i in range(lowLimit, (upLimit + 1), skip):
        if (board[i] == side):
            meCount += 1
        elif (board[i] == enemySide):
            enemyCount += 1

    # Assessing
    return scoreDictionary(meCount, enemyCount)

def scoreDictionary(meCount, enemyCount):
    score = meCount - enemyCount
    if (score == 4):
        return 6000
    elif (score == 3):
        return 80
    elif (score == 2):
        return 9
    elif (score == 1):
        return 3
    elif (score == 0):
        return 0
    elif (score == -1):
        return -3
    elif (score == -2):
        return -10
    elif (score == -3):
        return -100
    elif (score == -4):
        return -15000

# Menghitung nilai dari board sekarang
def countBoardValue(board, side):
    return countWinPossibility(board, side)

# Simple minimax algorithm with alpha-beta pruning
# -1 means the node is already terminal node and couldn't do anything more
# Function call:
# minimaxAlgorithm(board, <Depth Value < 42>, -math.Inf, +math.Inf, <computer Colour>, true)
def minimaxAlgorithm (board, depth, alpha, beta, side, maximizingPlayer, initSide):
    # If the board is full, return DRAW
    if (board.count(0) == 0):
        return (-1, 0)

    # If the node is terminal, count the end board value
    elif depth == 0:
        return (-1, countBoardValue(board, initSide))

    # Else, open up new nodes
    else:
        # Generating basic value
        value = 0
        bestPath = 0
        if (maximizingPlayer):
            value = -math.inf
        else:
            value = math.inf

        for i in range(1, 8):

            # Creating a new board with the child
            tempBoard = copy.copy(board)
            idx = util.fill(tempBoard, i, side)


            # If win, update the score
            if (util.checkWin(tempBoard, idx, side)):
                tempValue = countLastStone(board)
                if (side != initSide):
                    tempValue *= -10
                tempValue += countBoardValue(board,initSide)
                eval = (i, tempValue)

            # Else get next value
            else:
                # Getting other side
                newSide = 0
                if (side == util.WHITE):
                    newSide = util.BLACK
                else:
                    newSide = util.WHITE

                # Evaluation of the node
                eval = minimaxAlgorithm(tempBoard, (depth - 1), alpha, beta, newSide, not maximizingPlayer, initSide)

            # Implementing alpha beta pruning
            if (maximizingPlayer):
                if (eval[1] > value):
                    bestPath = i
                    value = eval[1]
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            else:
                if (eval[1] < value):
                    bestPath = i
                    value = eval[1]
                beta = min(beta, value)
                if beta <= alpha:
                    break

        return (bestPath, value)
