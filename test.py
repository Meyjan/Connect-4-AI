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

def main():
    side = -1
    while True:
        side = -side
        choice = int(input())
        fill(choice, side)
        # board[choice-1] = 1
        init = 35
        for i in range(len(board)):
            print(board[init+i], end = '')
            if(i % 7 == 6):
                print()
                init = init - 14

if __name__ == "__main__":
    main()
