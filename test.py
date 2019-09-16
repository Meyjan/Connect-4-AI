board = [0] * 42

Max_Row = 6
Max_Col = 7

def checkWin(lastIdx, side):
    turn = 1
    if(side == -1):
        turn = 2
    row = lastIdx % Max_Col
    col = lastIdx % Max_Row
    #Check horizontal
    for i in range(Max_Col - 3):
        for j in range(Max_Row):
            if board[j*Max_Col+i] == turn and board[j*Max_Col+i+1] == turn and board[j*Max_Col+i+2] == turn and board[j*Max_Col+i+3] == turn:
                return True

    #Check vertical
    for i in range(Max_Col):
        for j in range(Max_Row - 3):
            if board[j*Max_Col+i] == turn and board[(j+1)*Max_Col+i] == turn and board[(j+2)*Max_Col+i] == turn and board[(j+3)*Max_Col+i] == turn:
                return True

    #Check positive diagonal
    for i in range(Max_Col - 3):
        for j in range(Max_Row - 3):
            if board[j*Max_Col+i] == turn and board[(j+1)*Max_Col+i+1] == turn and board[(j+2)*Max_Col+i+2] == turn and board[(j+3)*Max_Col+i+3] == turn:
                return True

    #Check negative diagonal
    for i in range(Max_Col - 3):
        for j in range(3, Max_Row):
            if board[j*Max_Col+i] == turn and board[(j-1)*Max_Col+i+1] == turn and board[(j-2)*Max_Col+i+2] == turn and board[(j-3)*Max_Col+i+3] == turn:
                return True

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
    init = Max_Row * Max_Col - Max_Col
    for i in range(len(board)):
        print(board[init+i], end = '')
        if(i % Max_Col == Max_Col-1):
            print()
            init = init - (Max_Col * 2)

def main():
    side = -1
    while True:
        side = -side
        choice = int(input())
        chk = fill(choice, side)
        printBoard()
        if(checkWin(chk, side)):
            turn = "Black"
            if(side == -1):
                turn = "White"
            print(turn + " win")
            break

if __name__ == "__main__":
    main()
