import random
import os

def print_board():

    # Prints the game board.
    os.system('clear')
    print("      -----------------------------")
    for i in board:
        j = (i[0:])
        row = '      | ' + str(j[0]).rjust(4) + ' | ' + str(j[1]).rjust(4) + ' | ' + str(j[2]).rjust(4) + ' | ' + str(j[3]).rjust(4) + ' | '
        print(row)
        print("      -----------------------------")

def clear_board():
    
    #Clears the board.
    for i in range(len(board)):
        for j in range(4):
            board[i][j] = ""
    return board

def random_tile(n):

    # Start a new game with two initial random numbers which are either 2 or 4.
    #global game_end
    #game_end = ""
    rand_n = 0
    while True:
        b_row=random.randrange(4)
        b_col=random.randrange(4)
        if board[b_row][b_col]=="":
            x=random.randrange(5)
            if x < 4:
                board[b_row][b_col] = 2
            else:
                board[b_row][b_col] = 4
            rand_n += 1
        if rand_n == n:
            print_board()
            break
            


def win(tile_n):

    #The function checks if tile_n is in the table, if it is, it sets the game conditions to end the game as a winner.
    board_temp = []
    win_board = []
    for i in range(len(board)):
        board_temp = board[i][:]
        win_board[i:i]= board_temp
    if tile_n in win_board:
        global game_end
        game_end = "win"
        return tile_n in win_board
    return tile_n not in win_board

def board_full():

    #Checks if there is any empty tile on the board.
    for i in range(len(board)):
        for j in range(4):
            if board[i][j] == "":
                return False
    return True

def no_more_steps():

    #Checks if there are number pairs that can be merged or not.
    b_col=0
    rvar = True
    for i in range(4):
        b_row = i
        if board[b_row][b_col+1] == board[b_row][b_col] or board[b_row][b_col+2] == board[b_row][b_col+1] or board[b_row][b_col+3] == board[b_row][b_col+2]:
            if rvar != False:
                rvar = False
            if rvar == False:
                return rvar
    b_row=0
    for i in range(4):
        b_col = i
        if board[b_row][b_col] == board[b_row+1][b_col] or board[b_row+1][b_col] == board[b_row+2][b_col] or board[b_row+2][b_col] == board[b_row+3][b_col]:
            if rvar != False:
                rvar = False
            if rvar == False:
                return rvar
    return rvar

def game_state(n):

    #Sets the game condition to "lose" or "win" depending on the given criteria. 
    if board_full() == True and no_more_steps() == True:
        global game_end
        game_end = "lose"
        return
    if win(n) == False:
        game_end = "win"
        return
    

        
def game_logic():

    #The main script which does the moving and merging of the tiles according to the direction what the player entered. 
    print("{:<10} {:^20} {:>10}".format("w = up", "a = left", "x = quit"))
    print("{:<10} {:^22} {:>12}".format("s = down", "d = right", "n = new game"))
    ask=input("Enter direction:\n")
    if ask=="w":
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
                if board[b_row][b_col]==board[b_row+1][b_col]:
                    board[b_row][b_col]*=2
                    board[b_row+1][b_col]=""
            for j in range(3):
                b_row = j
                if board[b_row][b_col] == "":
                    board[b_row][b_col], board[b_row+1][b_col] = board[b_row+1][b_col], board[b_row][b_col]
        random_tile(1)

    if ask=="s":
        for i in range(4):
            b_col = i
            x = 0
            while x < 8:
                for j in range(1,4):
                    b_row = j
                    if board[b_row][b_col] == "":
                        board[b_row][b_col], board[b_row-1][b_col] = board[b_row-1][b_col], board[b_row][b_col]
                    x += 1
            for j in range(1,4):
                b_row = j
                if board[b_row][b_col]==board[b_row-1][b_col]:
                    board[b_row][b_col]*=2
                    board[b_row-1][b_col]=""
            for j in range(1,4):
                b_row = j
                if board[b_row][b_col] == "":
                    board[b_row][b_col], board[b_row-1][b_col] = board[b_row-1][b_col], board[b_row][b_col]
        random_tile(1)


    if ask=="a":
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
                if board[b_row][b_col]==board[b_row][b_col+1]:
                    board[b_row][b_col]*=2
                    board[b_row][b_col+1]=""
            for j in range(3):
                b_col = j
                if board[b_row][b_col] == "":
                    board[b_row][b_col], board[b_row][b_col+1] = board[b_row][b_col+1], board[b_row][b_col]
        random_tile(1)


    if ask=="d":
        for i in range(4):
            b_row = i
            x = 0
            while x < 8:
                for j in range(1,4):
                    b_col = j*-1
                    if board[b_row][b_col] == "":
                        board[b_row][b_col], board[b_row][b_col-1] = board[b_row][b_col-1], board[b_row][b_col]
                    x += 1
            for j in range(1,4):
                b_col = j*-1
                if board[b_row][b_col]==board[b_row][b_col-1]:
                    board[b_row][b_col]*=2
                    board[b_row][b_col-1]=""
            for j in range(1,4):
                b_col = j*-1
                if board[b_row][b_col] == "":
                    board[b_row][b_col], board[b_row][b_col-1] = board[b_row][b_col-1], board[b_row][b_col]
        random_tile(1)

    if ask == "x":
        exit()

    if ask == "n":
        clear_board()
        random_tile(2)
        print_board()


    else:
        pass


def game():

    # Main game loop.
    os.system('clear')
    while True:
        clear_board()
        random_tile(2)
        print_board()
        while game_end == "":
            game_logic()
            game_state(16)
            if game_end == "win":
                print("You have won 2048! Congratulations!")
                ask = input("Do you want to continue? [y/n]")
                if ask == "y":
                    global game_end
                    game_end = "continue"
                else:
                    exit()
        while game_end == "continue":
            game_logic()
            game_state(999)
        while game_end == "lose":
            print("You lost...")
            ask = input("Do you wish to start a new game? [y/n] ")
            if ask == "y":
                break
            else:
                exit()


board=[["","","",""],
       ["","","",""],
       ["","","",""],
       ["","","",""]
        ]   

game_end = ""
#b_row=0
#b_col=0
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