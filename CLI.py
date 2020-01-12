import Utility as util
import math
import AI_Random as ai_random
import AI_Smart as ai_smart

board = [0] * 42
#rumus akses data baris ke-i dan kolom ke-j:
# (i-1) * MAX_COLUMN + (j-1)

def main():
    first = False
    playerSide = int(input("Choose Side: \n1. Black\n2. White\n>> "))
    enemySide = 0
    if(playerSide == util.WHITE):
        first = True
        enemySide = util.BLACK
    else:
        enemySide = util.WHITE
    side = util.WHITE
    print()
    movement = 0
    if(first):
        movement = int(input("Column Number: "))
        while(not util.checkValidPosition(board, movement)):
            movement = int(input("Error. Enter a correct column number: "))

    else:
        movement, score = ai_smart.minimaxAlgorithm(board, 5, -math.inf, math.inf, enemySide, True, enemySide)
    idx = util.fill(board, movement, side)
    util.printBoard(board)
    print()

    while True:
        if(side == util.WHITE):
            side = util.BLACK
        else:
            side = util.WHITE
        if(side == playerSide):
            movement = int(input("Column Number: "))
            while(util.getOpenRowInColumn(board, movement) == -1):
                movement = int(input("Error. Enter a correct column number: "))
        else:
            movement, score = ai_smart.minimaxAlgorithm(board, 5, -math.inf, math.inf, enemySide, True, enemySide)
            print("EnemySide =", enemySide)
            print("Movement =", movement)
            print("Score =", score)
        idx = util.fill(board, movement, side)
        util.printBoard(board)
        print()
        if(util.checkWin(board, idx, side)):
            turn = "Black"
            if(side == util.WHITE):
                turn = "White"
            print(turn + " Side Win")
            break

if __name__ == "__main__":
    main()
