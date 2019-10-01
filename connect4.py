import numpy
import pygame
import sys

ROW = 6
COLUMN = 7
BOARD_COLOR = (0,0,200)
CIRCLE_COLOR = (0,0,0)
SQUARE = 75
RAD = 35
PLAYER_1 = (255,255,0)
PLAYER_2 = (255,0,0)

def makeBoard():
    board = numpy.zeros((6,7))
    return board

def draw(board):
    for i in range(ROW):
        for j in range(COLUMN):
            pygame.draw.rect(window,BOARD_COLOR,(j * SQUARE , i * SQUARE + SQUARE, SQUARE, SQUARE))
            if(board[i][j] == 0):
                pygame.draw.circle(window,CIRCLE_COLOR,(int(j * SQUARE + SQUARE/2),int(i * SQUARE + SQUARE + SQUARE/2)), RAD)
            elif(board[i][j] == 1):
                pygame.draw.circle(window,PLAYER_1,(int(j * SQUARE + SQUARE/2),int(i * SQUARE + SQUARE + SQUARE/2)), RAD)
            elif(board[i][j] == 2):
                pygame.draw.circle(window,PLAYER_2,(int(j * SQUARE + SQUARE/2),int(i * SQUARE + SQUARE + SQUARE/2)), RAD)
    pygame.display.update()

def checkZero(board,column):
    line = -1
    for i in range(5,-1,-1):
        if(board[i,column] == 0):
            line = i
            break
    return line

def turn(board,player,column):
    line = checkZero(board,column)
    if(line != -1):
        board[line,column] = player


# Main program
pygame.init()
width = COLUMN * SQUARE
height = (ROW + 1) * SQUARE

windowSize = (width , height)

window = pygame.display.set_mode(windowSize)
board = makeBoard()
draw(board)
pygame.display.update()
player = 1
gameOver = False

while not gameOver:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit()

        if(event.type == pygame.MOUSEMOTION):
            pygame.draw.rect(window,CIRCLE_COLOR,(0, 0, width, SQUARE))
            if(player == 1):
                pygame.draw.circle(window,PLAYER_1,(int(int(event.pos[0] / SQUARE) * SQUARE + SQUARE / 2),int(SQUARE/2)), RAD)
            elif(player == 2):
                pygame.draw.circle(window,PLAYER_2,(int(int(event.pos[0] / SQUARE) * SQUARE + SQUARE / 2),int(SQUARE/2)), RAD)
            pygame.display.update()

        if(event.type == pygame.MOUSEBUTTONDOWN):
            column = int(event.pos[0] / SQUARE)
            turn(board,player,column)
            draw(board)
            player = (player % 2) + 1