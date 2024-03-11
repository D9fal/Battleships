# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('battleship data')

battleships_positions = SHEET.worksheet('battleships_pos')
player_data = SHEET.worksheet('player')

ships_positions = battleships_positions.get_all_values()
player_d = player_data.get_all_values()


def game_set_up():
    """ 
        starting the game,
        chosing the game size 5X5, 10X10 ou 20X20  
        and the number of ships on the board
    """
    print("Wellcome to Fal Battleship ... \n")
    print("setting up the game ... \n")
    print("Please enter 1 for 5X5   game size \n")
    print("       enter 2 for 10X10 game size \n")
    print("       enter 3 for 20X20 game size \n")

    while True:
        game_size = input("Enter your choice here:")
        if game_size not in "123":
            print("your choice is wrong! Pick a number between 1, 2 or 3")
        else:
            break
    board,row_conv = drawing_board(game_size)

    return (board, row_conv, game_size)  

def drawing_board(game_size):
    """ 
        the board is a list of list. where ' ' is an empty place or water and 'X' is a battleship.
    """
    """ 
        The idea is to allow palyers to entre a combination of letter and number to define a position on the board. 
        for example A1 will be row 1, and 2nd postion in the row. 
    """ 

    board5 = [

    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    ]

    board10 = [

    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]

    board20 = [

    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]

    row_letters_number = [ 
        { 
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3,
            'E': 4,
        },
        { 
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3,
            'E': 4,
            'F': 5,
            'G': 6,
            'H': 7,
            'I': 8,
            'J': 9,
        },
        { 
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3,
            'E': 4,
            'F': 5,
            'G': 6,
            'H': 7,
            'I': 8,
            'J': 9,
            'K': 10,
            'L': 11,
            'M': 12,
            'N': 13,
            'O': 14,
            'P': 15,
            'Q': 16,
            'R': 17,
            'S': 18,
            'T': 19,
        }
        ]

    board = [board5, board10, board20]

    for i in range(len(board)+1):       
        if int(game_size) == i :             
            game_board = board[i-1]
            game_col_let_nber = row_letters_number[i-1]
    return (game_board, game_col_let_nber)    

def battleships_def_pos(game_size, game_col_conv, game_board):
    """ 
        the function will be used to determine if the battleship positions is chosing by a computer of the second players.
        If only one player, he would have to play with the computer. 
        if 2 players, players 1 will enter the positions of the battleships and the players 2 will have to play the game. 
    """
    print("Please choose 1 if you have someone to install the Battleships on the board for you\n")
    print("          or  2 if you want the computer to place the Battleships on the board \n")

    while True:
        nber_player = input("Enter your choice here:")
        if nber_player not in "12":
            print("your choice is wrong! Pick a number between 1 et 2")
        else:
            break

    if nber_player == "1":
        data_list_of_list = user_place_battleship(game_size, game_col_conv, game_board)
    elif nber_player == "2":
        data_list_of_list= computer_place_battleship(game_size, game_col_conv, game_board)
    else:
        pass

    return data_list_of_list

def user_place_battleship(game_size, game_col_conv, game_board):
    """ 
    """
    if game_size == "1":
        nber_ships = 5 
        entries_col = "column (A to E for 5x5):"
        entries_row = "row (1 to 5):"
    elif  game_size == "2":
        nber_ships = 10
        entries_col = "column (A to E for 10x10):"
        entries_row = "row (1 to 10):"
    elif game_size == "3":
        nber_ships = 20
        entries_col = "column (A to T for 20x20):"
        entries_row = "row (1 to 20):"
    else: 
        pass
    row_number_list = []
    column_number_list = []
    for n in range(nber_ships):
        while True:
            print("Where do you want ship ", n + 1, "?")
            column = input(f"{entries_col}").upper()
            row = input(f"{entries_row}") 
            if validate_battleships_positions_letter(nber_ships,column) and validate_battleships_positions_number(nber_ships,row):
                print("valid entries")                                   
                column_number = game_col_conv[column]        
                row_number = int(row) - 1  
                if already_used_position(game_board,row_number,column_number):                              
                    game_board[row_number][column_number] = 'X'  
                    row_number_list.append(row_number)
                    column_number_list.append(column)                    
                    break         
                                
    data_list_of_list = record_ships_pos(row_number_list,column_number_list) 
    print(data_list_of_list)

    for row in game_board:
        print(row)    

    return data_list_of_list

def computer_place_battleship(game_size, game_col_conv, game_board):
    """
    """

    if game_size == "1":
        nber_ships = 5 
    elif  game_size == "2":
        nber_ships = 10
    elif game_size == "3":
        nber_ships = 20
    else: 
        pass
    column_number_list = []
    row_number_list = []
    for n in range(nber_ships):        
        x_coord = random.randint(1, nber_ships)-1
        y_coord = random.randint(1, nber_ships)-1        
        game_board[x_coord][y_coord] = "X"
        for key,value in  game_col_conv.items():
            if  y_coord == value:
                column = key                
                column_number_list.append(column) 
        row_number_list.append(x_coord)

    data_list_of_list = record_ships_pos(row_number_list, column_number_list ) 

    for row in game_board:
        print(row)  
    
    return data_list_of_list

def validate_battleships_positions_letter(nber_ships,column):
    if nber_ships == 5:
        letter_span = "ABCDE"
    elif nber_ships == 10:
        letter_span = "ABCDEFGHIJ"
    else:
        letter_span = "ABCDEFGHIJKLMNOPQRST"

    try:
        if letter_span.find(column) == -1 :
            raise ValueError(f"{column} is not a letter between{letter_span}")

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

def validate_battleships_positions_number(nber_ships,row):
   
    try:
        if  int(row) > int(nber_ships):
            raise ValueError(f"{row} must be a number between 1 and {nber_ships}")

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False        
   
    return True

def already_used_position(game_board, row_number,column_number):
    try:
        if  game_board[row_number][column_number] == 'X' :
            raise ValueError(f" there is a battleship already in {column_number} {row_number}")

    except ValueError as e:
        print(f" duplicate data: {e}, please try again.\n")
        return False        
   
    return True


def player_enter_battleships_position():
    print("position")

def record_ships_pos(number, letter):
    data = []
    data_list_of_list = []
    for i in range(len(number)):    
        data_list_of_list.append([letter[i],number[i]])   
        data.append(letter[i])
        data.append(number[i])    
    battleships_positions.append_row(data) 
    return   data_list_of_list 

def guessing_play(game_size,game_col_conv,game_board, battleships_positions):

    """

    """
    
    if int(game_size) == 1:
        entries_col = "column ( Enter a letter between A to E):"
        entries_row = "row (1 to 5):"
        nber_ships = 5  
    elif int(game_size) == 2:
        entries_col = "column ( Enter a letter between A to J):"
        entries_row = "row (1 to 10):"
        nber_ships = 10
    elif int(game_size) == 3:
        nber_ships = 20 
        entries_col = "column ( Enter a letter between A to T):"
        entries_row = "row (1 to 20):"
    else:
        pass
    nber_guess = 1 
    print("Are you ready to start guessing the Ships position?:")
    start_ok = input(" type Yes to start : ")
    if start_ok.upper() == "YES":
        new_board = clear_game_board(nber_ships,game_board)
        while nber_guess <= nber_ships:
            print(f"Find the battleship number {nber_guess} here: ")
            column = input(f"{entries_col}").upper()
            row = input(f"{entries_row}")

            if validate_battleships_positions_letter(nber_ships,column) and validate_battleships_positions_number(nber_ships,row):
                print("valid entries")  
                column_number = int(game_col_conv[column])
                row_number = int(row) - 1 

                for i in range(nber_ships):
                    if not ((column == battleships_positions[i][0]) and (int(row_number) ==  int(battleships_positions[i][1]))):
                        continue                         
                    else: 
                        print("Good Guess!")
                        new_board[row_number][column_number] = "X"  
                        nber_guess = nber_guess +1  
                        break                 
                           
        #    print("Wrong Guess!")
        #    new_board[row_number][column_number] = "o" 

        print("END od The Game!")

def clear_game_board(nber_ships,game_board):
    for i in range(nber_ships):
        for j in range(nber_ships):
            if game_board[i][j] == "X":
                game_board[i][j] = " "
    
    for k in game_board:
        print(k)
    return game_board

def main():
    game_board, game_col_conv, game_size = game_set_up()
    battleships_positions = battleships_def_pos(game_size, game_col_conv,game_board)    
    guessing_play(game_size,game_col_conv,game_board, battleships_positions)
    
main()