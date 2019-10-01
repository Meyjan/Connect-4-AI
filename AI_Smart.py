import random
import Utility as util
import copy
import math

moveAIList = []

for i in range(util.MAX_COLUMN):
    moveAIList.append(i+1)

board = [0] * 42
board[2] = 1
board[3] = 1
board[4] = 1
board[5] = 2
board[6] = 2
board[0] = 2

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
    return remainingStones

# Menghitung jumlah kemenangan yang mungkin dimiliki oleh user
def countWinPossibility(board, columnPut):
    for ()
    return 0

# Menghitung nilai dari board sekarang
def countBoardValue(board):
    return 0

# Menghitung nilai dari board saat permainan selesai
def countEndBoardValue():
    # EDIT LAGI
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
        return (-1, countEndBoardValue())

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
            util.printBoard(tempBoard)

            # If win, update the score
            if (util.checkWin(tempBoard, -1, side)):
                tempValue = countLastStone(board)
                tempValue += countBoardValue(board)
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
                print("Max player")
                if (eval[1] > value):
                    bestPath = i
                    value = eval[1]
                alpha = max(alpha, value)
                if beta <= alpha:
                    print(alpha, beta)
                    print("alpha/beta cutoff")
                    break
            else:
                if (eval[1] < value):
                    bestPath = i
                    value = eval[1]
                beta = min(beta, value)
                if beta <= alpha:
                    print("alpha/beta cutoff")
                    break
        print("Alpha =", alpha, "Beta =", beta)

        return (bestPath, value)
                

minimaxAlgorithm(board, 3, -math.inf, math.inf, 1, True)