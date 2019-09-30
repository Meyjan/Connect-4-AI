import random
import Utility as util
moveAIList = []

for i in range(util.MAX_COLUMN):
    moveAIList.append(i+1)

def aiMove(board):
    move = random.choice(moveAIList)
    while(not util.checkValidPosition(board, move)):
        move = random.choice(moveAIList)
    return move
