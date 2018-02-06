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

def new_game():

    # Start a new game with two initial random numbers which are either 2 or 4.
    global game_end
    game_end = ""
    for i in range(2):
        b_row=random.randrange(4)
        b_col=random.randrange(4)
        if board[b_row][b_col]=="":
            x=random.randrange(5)
            if x < 4:
                board[b_row][b_col] = 2
            else:
                board[b_row][b_col] = 4
    print_board()


def win():

    #The function checks if 256 is in the table, if it is, it sets the game conditions to end the game as a winner.
    board_temp = []
    win_board = []
    for i in range(len(board)):
        board_temp = board[i][:]
        win_board[i:i]= board_temp
    if 256 in win_board:
        global game_end
        game_end = "win"
        return 256 in win_board
    return 256 not in win_board

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

def game_state():

    #Sets the game condition to "lose" or "win" depending on the given criteria. 
    if board_full() == True and no_more_steps() == True:
        global game_end
        game_end = "lose"
        return
    if win() == False:
        game_end = "win"
        return
    

        
def game_logic():

    #The main script which does the moving and merging of the tiles according to the direction what the player entered. 
    ask=input("Enter direction: ")
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
        
    while True:
        b_row=random.randrange(4)
        b_col=random.randrange(4)
        if board[b_row][b_col]=="":
            x=random.randrange(5)
            if x < 4:
                board[b_row][b_col] = 2
            else:
                board[b_row][b_col] = 4
            print_board()
            break
    if ask=="x":
        exit()


def game():

    # Main game loop.
    os.system('clear')
    game = True
    while game == True:
        print('1. Please enter m for start, or x for exit')
        start = input()
        if start == 'x':
            game = False
            exit()
        if start == 'm':
            clear_board()
            new_game()
        while game_end == "":
            game_logic()
            game_state()
        while game_end == "win":
            print("You have won 256! Congratulations!")
            break
        while game_end == "lose":
            print("You lost...")
            break


board=[["","","",""],
       ["","","",""],
       ["","","",""],
       ["","","",""]
        ]   

game_end = ""
b_row=0
b_col=0
game()