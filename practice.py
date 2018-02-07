from colored import fg, bg, attr
import os
import random
from time import sleep


def print_board(board):
    
    # Prints the game board.
    os.system('clear')
    for i in board:
        j = (i[0:])
        c = 0
        clist = [250,250,250,250]
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
        row = '     %s%s %s{:>5} %s'.format(str(j[0])) %(fg(255), bg(c1), attr(1), attr(0)) \
              + '%s%s %s{:>5} %s'.format(str(j[1])) %(fg(255), bg(c2), attr(1), attr(0)) \
              + '%s%s %s{:>5} %s'.format(str(j[2])) %(fg(255), bg(c3), attr(1), attr(0)) \
              + '%s%s %s{:>5} %s'.format(str(j[3])) %(fg(255), bg(c4), attr(1), attr(0))
        print("     %s%s       %s%s       %s%s       %s%s       %s" 
              % (fg(c1), bg(c1), fg(c2), bg(c2), fg(c3), bg(c3), fg(c4), bg(c4), attr(0)))       
        print(row)
        print("     %s%s       %s%s       %s%s       %s%s       %s" 
              % (fg(c1), bg(c1), fg(c2), bg(c2), fg(c3), bg(c3), fg(c4), bg(c4), attr(0)))


def clear_board():
    board = [['']*4 for i in range(4)]
    return board


def rotate_board(board, r):
    # rotates the board
    while r > 0:
        board = list(map(list, zip(*board[::-1])))
        r -= 1
    return board


def random_tile(board, n):

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
            break


def main():
    board = [['']*4 for i in range(4)]
    random_tile(board, 2)
    print_board(board)
    while True:
        direction = ['D', 'W', 'A', 'S']
        rotate = input('enter A, W, D, S\n').upper()
        r = direction.index(rotate)
        board = rotate_board(board, r)
        moving(board)
        board = rotate_board(board, 4-r)
        print_board(board)
        sleep(0.1)
        random_tile(board, 1)
        print_board(board)


def moving(board):
    
    # The main script which does the moving and merging of the tiles according to the direction what the player entered.
    #score_ = 0
    #print("{:<10} {:^20} {:>10}".format("w = up", "a = left", "x = quit"))
    #print("{:<10} {:^22} {:>12}".format("s = down", "d = right", "n = new game"))
    #ask = input("Enter direction:\n")
    #if ask == "w":
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
                #if type(board[b_row][b_col]) is int:
                #    score_ += board[b_row][b_col]
                #    print(score_)
                board[b_row][b_col-1] = ""
        for j in range(1, 4):
            b_col = j*-1
            if board[b_row][b_col] == "":
                board[b_row][b_col], board[b_row][b_col-1] = board[b_row][b_col-1], board[b_row][b_col]


os.system('clear')
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
    main()

