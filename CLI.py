import Utility as util

board = [0] * 42

def fill(number, side):
    i = number - 1
    while i < len(board):
        if(board[i] == 0):
            board[i] = side
            break
        else:
            i += 7
    return i

def printBoard():
    init = util.MAX_ROW * util.MAX_COLUMN - util.MAX_COLUMN
    for i in range(len(board)):
        print(board[init+i], end = '')
        if(i % util.MAX_COLUMN == util.MAX_COLUMN-1):
            print()
            init = init - (util.MAX_COLUMN * 2)

def main():
    side = util.WHITE
    while True:
        if(side == util.WHITE):
            side = util.BLACK
        else:
            side = util.WHITE
        userInput = int(input("Column Number: "))
        idx = fill(userInput, side)
        printBoard()
        print()
        if(util.checkWin(board, idx, side)):
            turn = "Black"
            if(side == util.WHITE):
                turn = "White"
            print(turn + " Side Win")
            break

if __name__ == "__main__":
    main()
