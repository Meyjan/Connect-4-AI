import Utility as util
import AI_Random as ai_random

board = [0] * 42
#rumus akses data baris ke-i dan kolom ke-j:
# (i-1) * MAX_COLUMN + (j-1)

def main():
    first = False
    playerSide = int(input("Choose Side: \n1. Black\n2. White\n>> "))
    if(playerSide == util.WHITE):
        first = True
    side = util.WHITE
    print()
    movement = 0
    if(first):
        movement = int(input("Column Number: "))
        while(not util.checkValidPosition(board, movement)):
            movement = int(input("Error. Enter a correct column number: "))

    else:
        movement = ai_random.aiMove(board)
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
            movement = ai_random.aiMove(board)
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
