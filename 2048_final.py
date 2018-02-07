import random
import os
from colored import fg, bg, attr
from time import sleep


def print_board():

    # Prints the game board.
    os.system('clear')
    for i in board:
        j = (i[0:])
        c = 0
        clist = [250, 250, 250, 250]
        for k in board:
            j = (i[0:])
            c = 0
            for l in range(4):
                if j[l] == 2:
                    clist[l] = 240
                if j[l] == 4:
                    clist[l] = 235
                if j[l] == 8:
                    clist[l] = 212
                if j[l] == 16:
                    clist[l] = 211
                if j[l] == 32:
                    clist[l] = 210
                if j[l] == 64:
                    clist[l] = 209
                if j[l] == 128:
                    clist[l] = 216
                if j[l] == 256:
                    clist[l] = 215
                if j[l] == 512:
                    clist[l] = 214
                if j[l] == 1024:
                    clist[l] = 83
                if j[l] == 2048:
                    clist[l] = 82
                if j[l] == 4096:
                    clist[l] = 4
                if j[l] == 8192:
                    clist[l] = 27
                if j[l] == 16384:
                    clist[l] = 21
                if j[l] == 32768:
                    clist[l] = 20
                if j[l] == 65536:
                    clist[l] = 19
        c1 = clist[0]
        c2 = clist[1]
        c3 = clist[2]
        c4 = clist[3]
        row = '     %s%s %s{:>5} %s'.format(str(j[0])) % (fg(255), bg(c1), attr(1), attr(0)) \
              + '%s%s %s{:>5} %s'.format(str(j[1])) % (fg(255), bg(c2), attr(1), attr(0)) \
              + '%s%s %s{:>5} %s'.format(str(j[2])) % (fg(255), bg(c3), attr(1), attr(0)) \
              + '%s%s %s{:>5} %s'.format(str(j[3])) % (fg(255), bg(c4), attr(1), attr(0))
        print("     %s%s       %s%s       %s%s       %s%s       %s"
              % (fg(c1), bg(c1), fg(c2), bg(c2), fg(c3), bg(c3), fg(c4), bg(c4), attr(0)))
        print(row)
        print("     %s%s       %s%s       %s%s       %s%s       %s"
              % (fg(c1), bg(c1), fg(c2), bg(c2), fg(c3), bg(c3), fg(c4), bg(c4), attr(0)))


def clear_board():

    # Clears the board.
    for i in range(len(board)):
        for j in range(4):
            board[i][j] = ""
    return board


def random_tile(n):

    # Inserts random number into a random tile.
    rand_n = 0
    while True:
        b_row = random.randrange(4)
        b_col = random.randrange(4)
        if board[b_row][b_col] == "":
            x = random.randrange(5)
            if x < 4:
                board[b_row][b_col] = 2
            else:
                board[b_row][b_col] = 4
            rand_n += 1
        if rand_n == n:
            print_board()
            break


def win(tile_n):

    # The function checks if tile_n is in the table, if it is, it sets the game conditions to end the game as a winner.
    for i in range(len(board)):
        if tile_n in board[i]:
            return True
    return False


def board_full():

    # Checks if there is any empty tile on the board.
    for i in range(len(board)):
        for j in range(4):
            if board[i][j] == "":
                return False
    return True


def no_more_steps():

    # Checks if there are number pairs that can be merged or not.
    b_col = 0
    rvar = True
    for i in range(4):
        b_row = i
        if board[b_row][b_col+1] == board[b_row][b_col] \
           or board[b_row][b_col+2] == board[b_row][b_col+1] or board[b_row][b_col+3] == board[b_row][b_col+2]:
            if rvar is not False:
                rvar = False
            if rvar is False:
                return rvar
    b_row = 0
    for i in range(4):
        b_col = i
        if board[b_row][b_col] == board[b_row+1][b_col] \
           or board[b_row+1][b_col] == board[b_row+2][b_col] or board[b_row+2][b_col] == board[b_row+3][b_col]:
            if rvar is not False:
                rvar = False
            if rvar is False:
                return rvar
    return rvar


def game_logic():
    
    # The main script which does the moving and merging of the tiles according to the direction what the player entered.
    score_ = 0
    print("{:<10} {:^20} {:>10}".format("w = up", "a = left", "x = quit"))
    print("{:<10} {:^22} {:>12}".format("s = down", "d = right", "n = new game"))
    ask = input("Enter direction:\n")
    if ask == "w":
        for i in range(4):
            b_col = i
            x = 0
            while x < 8:
                for j in range(3):
                    b_row = j
                    if board[b_row][b_col] == "":
                        board[b_row][b_col], board[b_row+1][b_col] = board[b_row+1][b_col], board[b_row][b_col]
                    x += 1
            for j in range(3):
                b_row = j
                if board[b_row][b_col] == board[b_row+1][b_col]:
                    board[b_row][b_col] *= 2
                    if type(board[b_row][b_col]) is int:
                        score_ += board[b_row][b_col]
                        print(score_)
                    board[b_row+1][b_col] = ""
            for j in range(3):
                b_row = j
                if board[b_row][b_col] == "":
                    board[b_row][b_col], board[b_row+1][b_col] = board[b_row+1][b_col], board[b_row][b_col]
        print_board()
        sleep(0.1)
        random_tile(1)

    if ask == "s":
        for i in range(4):
            b_col = i
            x = 0
            while x < 8:
                for j in range(1, 4):
                    b_row = j
                    if board[b_row][b_col] == "":
                        board[b_row][b_col], board[b_row-1][b_col] = board[b_row-1][b_col], board[b_row][b_col]
                    x += 1
            for j in range(1, 4):
                b_row = j
                if board[b_row][b_col] == board[b_row-1][b_col]:
                    board[b_row][b_col] *= 2
                    if type(board[b_row][b_col]) is int:
                        score_ += board[b_row][b_col]
                        print(score_)
                    board[b_row-1][b_col] = ""
            for j in range(1, 4):
                b_row = j
                if board[b_row][b_col] == "":
                    board[b_row][b_col], board[b_row-1][b_col] = board[b_row-1][b_col], board[b_row][b_col]
        print_board()
        sleep(0.1)
        random_tile(1)

    if ask == "a":
        for i in range(4):
            b_row = i
            x = 0
            while x < 8:
                for j in range(3):
                    b_col = j
                    if board[b_row][b_col] == "":
                        board[b_row][b_col], board[b_row][b_col+1] = board[b_row][b_col+1], board[b_row][b_col]
                    x += 1
            for j in range(3):
                b_col = j
                if board[b_row][b_col] == board[b_row][b_col+1]:
                    board[b_row][b_col] *= 2
                    if type(board[b_row][b_col]) is int:
                        score_ += board[b_row][b_col]
                        print(score_)
                    board[b_row][b_col+1] = ""
            for j in range(3):
                b_col = j
                if board[b_row][b_col] == "":
                    board[b_row][b_col], board[b_row][b_col+1] = board[b_row][b_col+1], board[b_row][b_col]
        print_board()
        sleep(0.1)
        random_tile(1)

    if ask == "d":
        for i in range(4):
            b_row = i
            x = 0
            while x < 8:
                for j in range(1, 4):
                    b_col = j*-1
                    if board[b_row][b_col] == "":
                        board[b_row][b_col], board[b_row][b_col-1] = board[b_row][b_col-1], board[b_row][b_col]
                    x += 1
            for j in range(1, 4):
                b_col = j*-1
                if board[b_row][b_col] == board[b_row][b_col-1]:
                    board[b_row][b_col] *= 2
                    if type(board[b_row][b_col]) is int:
                        score_ += board[b_row][b_col]
                        print(score_)
                    board[b_row][b_col-1] = ""
            for j in range(1, 4):
                b_col = j*-1
                if board[b_row][b_col] == "":
                    board[b_row][b_col], board[b_row][b_col-1] = board[b_row][b_col-1], board[b_row][b_col]
        print_board()
        sleep(0.1)
        random_tile(1)

    if ask == "x":
        exit()

    if ask == "n":
        clear_board()
        random_tile(2)
        print_board()

    return score_


def game():
    # Main game loop.
    os.system('clear')
    while True:
        clear_board()
        random_tile(2)
        print_board()
        score_ = 0
        while True:
            score_ += game_logic()
            print(score_)
            if win(16):
                print("You have won 2048! Congratulations!")
                ask = input("Do you want to continue? [y/n]")
                if ask == "y":
                    break
                else:
                    exit()
            if board_full() and no_more_steps():
                print("You lost...")
                ask = input("Do you wish to start a new game? [y/n] ")
                if ask == "y":
                    break
                else:
                    exit()
        while True:
            score_ += game_logic()
            print(score_)
            if board_full() and no_more_steps():
                print("You lost...")
                ask = input("Do you wish to start a new game? [y/n] ")
                if ask == "y":
                    break
                else:
                    exit()


board = [["", "", "", ""],
         ["", "", "", ""],
         ["", "", "", ""],
         ["", "", "", ""]
         ]

clear_board()
print("""
        Welcome to the game '2048'!

        The goal of the game is to join the numbers and get the tile 2048.
        Controls:
        w - move the tiles up
        s - move the tiles down
        a - move the tiles left
        d - move the tiles right
        
        x - quit the game
        """
      )
start = input('Please enter "s" for start, or "x" for exit:\n')
if start == 'x':
    exit()
if start == 's':
    game()
