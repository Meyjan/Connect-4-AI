import Utility as util

board = [0] * 42


def fill(number, side):
    i = number - 1
    while i < len(board):
        if(board[i] == 0):
            if(side == -1):
                board[i] = 2
            else:
                board[i] = 1
            break
        else:
            i += 7
    return i


def printBoard():
    init = util.MAX_ROW * util.MAX_COLUMN - util.MAX_COLUMN
    for i in range(len(board)):
        print(board[init+i], end='')
        if(i % util.MAX_COLUMN == util.MAX_COLUMN-1):
            print()
            init = init - (util.MAX_COLUMN * 2)


def main():
    side = -1
    while True:
        side = -side
        choice = int(input())
        chk = fill(choice, side)
        printBoard()
        if(util.checkWin(board, chk, side)):
            turn = "Black"
            if(side == -1):
                turn = "White"
            print(turn + " win")
            break


if __name__ == "__main__":
    main()
