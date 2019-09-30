import random
import Utility as util
import copy

moveAIList = []

for i in range(util.MAX_COLUMN):
    moveAIList.append(i+1)

board = [0] * 42
board[3] = 1
board[2] = -1

# Board menggambarkan state board sekarang
# aiNumber merupakan nomor AI yang direpresentasikan oleh board
def aiMove(board, side):
    move = random.choice(moveAIList)
    while(not util.checkValidPosition(board, move)):
        move = random.choice(moveAIList)
    return move

# Menghitung jumlah langkah yang dibutuhkan sampai batu terakhir ditetapkan
def countLastStone(board):
    remainingStones = board.count(0)
    remainingStones = remainingStones // 2 + remainingStones % 2
    print(remainingStones)


def countEndBoardValue():
    # EDIT LAGI
    return 0

# Simple minimax algorithm
def minimaxAlgorithm(board, depth, side):
    if (depth == 0):
        countEndBoardValue()
    else:
        result = []
        for i in range (1, 8):
            tempBoard = copy.deepcopy(board)
            idx = util.fill(tempBoard, i, side)
            if util.checkWin(tempBoard, idx, side):
                return countLastStone(tempBoard)
            else:
                nextSide = 0
                if (side == util.WHITE):
                    nextSide = util.BLACK
                else:
                    nextSide = util.WHITE
                result.append(minimaxAlgorithm(tempBoard, (depth - 1), nextSide))
        return max(result)
                


