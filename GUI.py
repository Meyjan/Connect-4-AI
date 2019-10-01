import math
import numpy
import pygame
import pygameMenu
import sys
import time
import Utility as util
import AI_Random as ai_random
import AI_Smart as ai_smart

BOARD_COLOR = (112,112,112)
CIRCLE_COLOR = (163,163,163)
SQUARE = 75
RAD = 35
PLAYER_1 = (0,0,0)
PLAYER_2 = (255,255,255)

COLOR_BACKGROUND = (128, 0, 128)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
PLAYER1 = ['USER']
PLAYER2 = ['USER']
FPS = 60.0
MENU_BACKGROUND_COLOR = (228, 55, 36)
WINDOW_SIZE = (640, 480)

clock = None
main_menu = None
window = None

def map(board):
    resBoard = numpy.zeros((util.MAX_ROW, util.MAX_COLUMN))
    j = 0
    for i in range(len(board)):
        row = i // util.MAX_COLUMN
        j = i % util.MAX_COLUMN
        resBoard[row][j] = board[i]
    resBoard = numpy.flipud(resBoard)
    return resBoard

def makeBoard():
    board = numpy.zeros((util.MAX_ROW, util.MAX_COLUMN))
    return board

def draw(board, window):
    for i in range(util.MAX_ROW):
        for j in range(util.MAX_COLUMN):
            pygame.draw.rect(window,BOARD_COLOR,(j * SQUARE , i * SQUARE + SQUARE, SQUARE, SQUARE))
            if(board[i][j] == 0):
                pygame.draw.circle(window,CIRCLE_COLOR,(int(j * SQUARE + SQUARE/2),int(i * SQUARE + SQUARE + SQUARE/2)), RAD)
            elif(board[i][j] == 1):
                pygame.draw.circle(window,PLAYER_1,(int(j * SQUARE + SQUARE/2),int(i * SQUARE + SQUARE + SQUARE/2)), RAD)
            else:
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
    return line

def fun():
    pass

def menu_bg():
    """
    Background color of the main menu, on this function user can plot
    images, play sounds, etc.
    """
    global window
    global COLOR_BACKGROUND
    window.fill(COLOR_BACKGROUND)

def pick_player_1(value, player1):
    """
    Change difficulty of the game.
    :param value: Tuple containing the data of the selected object
    :type value: tuple
    :param difficulty: Optional parameter passed as argument to add_selector
    :type difficulty: basestring
    :return: None
    """
    selected, index = value
    print('Selected Bot: "{0}" ({1}) at index {2}'.format(selected, player1, index))
    PLAYER1[0] = player1

def pick_player_2(value, player2):
    """
    Change difficulty of the game.
    :param value: Tuple containing the data of the selected object
    :type value: tuple
    :param difficulty: Optional parameter passed as argument to add_selector
    :type difficulty: basestring
    :return: None
    """
    selected, index = value
    print('Selected side: "{0}" ({1}) at index {2}'.format(selected, player2, index))
    PLAYER2[0] = player2

def play_function(player1, player2, font, test=False):
    """
    Main game function.
    :param difficulty: Difficulty of the game
    :type difficulty: basestring
    :param font: Pygame font
    :type font: pygame.font.FontType
    :param test: Test method, if true only one loop is allowed
    :type test: bool
    :return: None
    """
    assert isinstance(player1, (tuple, list))
    player1 = player1[0]
    assert isinstance(player1, str)

    assert isinstance(player2, (tuple, list))
    player2 = player2[0]
    assert isinstance(player2, str)

    # Define globals
    global main_menu
    global clock

    f = font.render(player1 + " WINS", 1, COLOR_WHITE)
    g = font.render(player2 + " WINS", 1, COLOR_WHITE)

    # Draw random color and text
    bg_color = COLOR_BACKGROUND
    f_width = f.get_size()[0]
    g_width = g.get_size()[0]
    # Reset main menu and disable
    # You also can set another menu, like a 'pause menu', or just use the same
    # main_menu as the menu that will check all your input.
    main_menu.disable()
    main_menu.reset(1)

    width = util.MAX_COLUMN * SQUARE
    height = (util.MAX_ROW + 1) * SQUARE

    windowSize = (width , height)

    window2 = pygame.display.set_mode(windowSize)

    side = [0] * 2
    idx = 0
    score = 0
    win = 0

    board1 = [0] * util.MAX_ROW * util.MAX_COLUMN
    board2 = makeBoard()

    player_1 = 0
    player_2 = 0
    playerSide = 0
    enemySide = 0
    if (player1 == "USER"):
        player_1 = util.PLAYER
        playerSide = util.BLACK
    elif (player1 == "RANDOM"):
        enemySide = util.WHITE
        player_1 = util.BOT_RANDOM
        playerSide = util.WHITE
        enemySide = util.BLACK
    else:
        player_1 = util.BOT_MINIMAX
        playerSide = util.WHITE
        enemySide = util.BLACK

    if(player2 == "USER"):
        player_2 = util.PLAYER
        playerSide = util.WHITE
        enemySide = util.BLACK
    elif (player2 == "RANDOM"):
        player_2 = util.BOT_RANDOM
        playerSide = util.BLACK
        enemySide = util.WHITE
    else:
        player_2 = util.BOT_MINIMAX
        playerSide = util.BLACK
        enemySide = util.WHITE

    gameOver = False

    side[0] = player_1
    side[1] = util.BLACK

    draw(board2, window)
    pygame.display.update()

    while not gameOver:
        # Clock tick
        clock.tick(60)

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and main_menu.is_disabled():
                    main_menu.enable()

            if (side[0] == util.PLAYER):
                if(event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONUP):
                    pygame.draw.rect(window2,CIRCLE_COLOR,(0, 0, width, SQUARE))
                    if (player_1 == util.PLAYER):
                        pygame.draw.circle(window2,PLAYER_1,(int(int(event.pos[0] / SQUARE) * SQUARE + SQUARE / 2),int(SQUARE/2)), RAD)
                    else:
                        pygame.draw.circle(window2,PLAYER_2,(int(int(event.pos[0] / SQUARE) * SQUARE + SQUARE / 2),int(SQUARE/2)), RAD)
                    pygame.display.update()

                if(event.type == pygame.MOUSEBUTTONDOWN):
                    column = int(event.pos[0] / SQUARE) + 1
                    idx = util.fill(board1, column, side[1])
                    util.printBoard(board1)
                    board2 = map(board1)
                    draw(board2, window2)
                    if (util.checkWin(board1, idx, side[1])):
                        gameOver = True
                        win = "USER"
                        time.sleep(3)
                    if (idx < util.MAX_ROW * util.MAX_COLUMN):
                        if (player_1 == util.PLAYER):
                            side[0] = player_2
                            side[1] = (side[1] % 2) + 1
                        else:
                            side[0] = player_1
                            side[1] = (side[1] % 2) + 1

            else:
                if (side[0] == util.BOT_RANDOM):
                    move = ai_random.aiMove(board1)
                    idx = util.fill(board1, move, side[1])
                    util.printBoard(board1)
                    board2 = map(board1)
                    draw(board2, window2)
                    if (util.checkWin(board1, idx, side[1])):
                        gameOver = True
                        win = "RANDOM BOT"
                        time.sleep(3)
                    if (idx < util.MAX_ROW * util.MAX_COLUMN):
                        if (player_1 == util.BOT_RANDOM):
                            side[0] = player_2
                            side[1] = (side[1] % 2) + 1
                        else:
                            side[0] = player_1
                            side[1] = (side[1] % 2) + 1
                else:
                    move, score = ai_smart.minimaxAlgorithm(board1, 5, -math.inf, math.inf, enemySide, True, enemySide)
                    idx = util.fill(board1, move, side[1])
                    util.printBoard(board1)
                    board2 = map(board1)
                    draw(board2, window2)
                    if (util.checkWin(board1, idx, side[1])):
                        gameOver = True
                        win = "AI BOT"
                        time.sleep(3)
                    if (idx < util.MAX_ROW * util.MAX_COLUMN):
                        if (player_1 == util.BOT_MINIMAX):
                            side[0] = player_2
                            side[1] = (side[1] % 2) + 1
                        else:
                            side[0] = player_1
                            side[1] = (side[1] % 2) + 1



        # Pass events to main_menu
        main_menu.mainloop(events)

        # Continue playing
        # window.fill(bg_color)
        # window.blit(f, ((WINDOW_SIZE[0] - f_width) / 2, WINDOW_SIZE[1] / 2))
        pygame.display.flip()

        # If test returns
        if test:
            break

    windowSize = (640 , 480)

    window3 = pygame.display.set_mode(windowSize)

    f = font.render(win + " WINS", 1, COLOR_WHITE)
    window.fill(bg_color)
    window.blit(f, ((WINDOW_SIZE[0] - f_width) / 2, WINDOW_SIZE[1] / 2))

def main():
    global clock
    global main_menu
    global window
    global COLOR_BACKGROUND


    pygame.init()
    # width = util.MAX_COLUMN * SQUARE
    # height = (util.MAX_ROW + 1) * SQUARE
    windowSize = (640, 480)

    window = pygame.display.set_mode(windowSize)
    clock = pygame.time.Clock()

    menu_play =  pygameMenu.Menu(window,
                    bgfun=menu_bg,
                    color_selected=COLOR_WHITE,
                    font=pygameMenu.font.FONT_BEBAS,
                    font_color=COLOR_BLACK,
                    font_size=30,
                    menu_alpha=100,
                    menu_color=MENU_BACKGROUND_COLOR,
                    menu_height=int(WINDOW_SIZE[1] * 0.7),
                    menu_width=int(WINDOW_SIZE[0] * 0.7),
                    onclose=pygameMenu.events.DISABLE_CLOSE,
                    option_shadow=False,
                    title='Play Menu',
                    window_height=WINDOW_SIZE[1],
                    window_width=WINDOW_SIZE[0]
                    )

    menu_play.add_option('Start',
                              play_function,
                              PLAYER1,
                              PLAYER2,
                              pygame.font.Font(pygameMenu.font.FONT_FRANCHISE, 30))
    menu_play.add_selector('Player 1',
                                [('User', 'USER'),
                                 ('Random', 'RANDOM'),
                                 ('AI', 'AI')],
                                onchange=pick_player_1,
                                selector_id='player_1')
    menu_play.add_selector('Player 2',
                                [('User', 'USER'),
                                 ('Random', 'RANDOM'),
                                 ('AI', 'AI')],
                                onchange=pick_player_2,
                                selector_id='player_2')
    menu_play.add_option('Back', pygameMenu.events.BACK) # Add exit function


    menu_play.set_fps(FPS)

    main_menu = pygameMenu.Menu(window,
                                   bgfun=menu_bg,
                                   color_selected=COLOR_WHITE,
                                   font=pygameMenu.font.FONT_BEBAS,
                                   font_color=COLOR_BLACK,
                                   font_size=30,
                                   menu_alpha=100,
                                   menu_color=MENU_BACKGROUND_COLOR,
                                   menu_height=int(WINDOW_SIZE[1] * 0.5),
                                   menu_width=int(WINDOW_SIZE[0] * 0.7),
                                   option_shadow=False,
                                   title='Main Menu',
                                   window_height=WINDOW_SIZE[1],
                                   window_width=WINDOW_SIZE[0]
                                   )
    main_menu.add_option('Play', menu_play)
    main_menu.add_option('Quit', pygameMenu.events.CLOSE)

    menu_play.draw()

    pygame.display.update()
    while True:

        # Tick
        clock.tick(FPS)

        # Paint background
        # menu_bg()

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        # Main menu
        main_menu.mainloop(events, disable_loop=False)

        # Flip surface
        pygame.display.flip()


if __name__ == '__main__':
    main()
