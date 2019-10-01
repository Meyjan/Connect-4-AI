import random
import Utility as util
import copy
import math

moveAIList = []

for i in range(util.MAX_COLUMN):
    moveAIList.append(i+1)

board = [0] * 42
board[3] = 1
board[4] = 1
board[5] = 2
board[6] = 2
board[0] = 2
board[10] = 1

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
    return (remainingStones * 1000)

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
        for j in range(1, util.MAX_COLUMN - 3):
            lowerLimit = util.getArrayIndex(i, j)
            upperLimit = util.getArrayIndex(i, j + 3)
            totalScore += scoreAssessing(board, side, enemySide, lowerLimit, upperLimit, 1)

    # Vertical check
    for i in range(1, util.MAX_COLUMN + 1):
        for j in range(1, util.MAX_ROW - 3):
            lowerLimit = util.getArrayIndex(j, i)
            upperLimit = util.getArrayIndex(j + 3, i)
            totalScore += scoreAssessing(board, side, enemySide, lowerLimit, upperLimit, 7)
    
    # Diagonal ascending check
    for i in range(1, util.MAX_ROW - 3):
        for j in range(1, util.MAX_COLUMN - 3):
            lowerLimit = util.getArrayIndex(i, j)
            upperLimit = util.getArrayIndex(i + 3, j + 3)
            totalScore += scoreAssessing(board, side, enemySide, lowerLimit, upperLimit, 8)

    # Diagonal descending check
    for i in range(1, util.MAX_ROW - 3):
        for j in range(4, util.MAX_COLUMN + 1):
            lowerLimit = util.getArrayIndex(i, j)
            upperLimit = util.getArrayIndex(i - 3, j - 3)
            totalScore += scoreAssessing(board, side, enemySide, lowerLimit, upperLimit, 6)
    
    print(totalScore)
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
        return 10000
    elif (score == 3):
        return 100
    elif (score == 2):
        return 10
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
        return -10000

# Menghitung nilai dari board sekarang
def countBoardValue(board, side):
    # return countWinPossibility
    return 0

# Menghitung nilai dari board saat permainan selesai
def countEndBoardValue(board, column, side):
    total = countWinPossibility(board, column, side)
    return 0

# Simple minimax algorithm with alpha-beta pruning
# -1 means the node is already terminal node and couldn't do anything more
# Function call:
# minimaxAlgorithm(board, <Depth Value < 42>, -math.Inf, +math.Inf, <computer Colour>, true)
def minimaxAlgorithm (board, depth, alpha, beta, side, maximizingPlayer):
    # If the board is full, return DRAW
    if (board.count(0) == 0):
        return (-1, 0)

    # If the node is terminal, count the end board value
    elif depth == 0:
        return (-1, countBoardValue(board, side))

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
            print("Depth = ", depth, "Path = ", i)

            # Creating a new board with the child
            tempBoard = copy.copy(board)
            idx = util.fill(tempBoard, i, side)

            # If win, update the score
            if (util.checkWin(tempBoard, idx, side)):
                tempValue = countLastStone(board)
                tempValue += countBoardValue(board)
                if not maximizingPlayer:
                    tempValue *= -1
                eval = (i, tempValue)
            
            else:
                # Getting other side
                newSide = 0
                if (side == util.WHITE):
                    newSide = util.BLACK
                else:
                    newSide = util.WHITE

                # Evaluation of the node
                eval = minimaxAlgorithm(tempBoard, (depth - 1), alpha, beta, newSide, not maximizingPlayer)
            
            # Implementing alpha beta pruning
            if (maximizingPlayer):
                if (eval[1] > value):
                    bestPath = i
                    value = eval[1]
                alpha = max(alpha, value)
                if beta <= alpha:
                    print(alpha, beta)
                    print("alpha/beta max cutoff in depth:", depth, "column", i, "side", side)
                    break
            else:
                if (eval[1] < value):
                    bestPath = i
                    value = eval[1]
                beta = min(beta, value)
                if beta <= alpha:
                    print("alpha/beta min cutoff in depth:", depth, "column", i, "side", side)
                    break
        print("Alpha =", alpha, "Beta =", beta)

        return (bestPath, value)
                

#minimaxAlgorithm(board, 3, -math.inf, math.inf, 1, True)
util.printBoard(board)
countWinPossibility(board, 1)