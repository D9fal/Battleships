# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import os

# import asciimatics

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

    This function takes "1", "2", "3" as argument and returns
    the layout of the game board (size, and rows and colums ranges)  
    """

    print("Wellcome to Fal Battleship ... \n")
    print("setting up the game ... \n")
    print("Please enter 1 for 5X5   game size \n")
    print("       enter 2 for 10X10 game size \n")
    print("       enter 3 for 20X20 game size \n")

    while True:
        game_size = input("Enter your choice here:")
        if game_size not in ["1", "2", "3"]:
            print("your choice is wrong! Pick a number between 1, 2 or 3")
        else:
            break
    board, row_conv = drawing_board(game_size)

    return (board, row_conv, game_size)


def drawing_board(game_size):

    """
    Once the game size is decided, this function 
    returns the specifics of the layouts.

    the board is a list of list. where ' ' is an
    empty place or water and 'X' is a battleship.
    
    The function is also called to convert the computer 
    understanding of matrix position to the the player understanding.
    for example:  
    The idea is to allow palyers to enter a combination
    of letter and number to define a position on the board.
    for example A1 is the position (0,0) on the matrix.
    """

    board5 = [
        ['_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_'],
        ]

    board10 = [
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ]

    board20 = [

        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_', '_', '_', '_'],
        ]

    row_letters_number = [
        {
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3,
            'E': 4,
        },        {
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
        },        {
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
        if int(game_size) == i:
            game_board = board[i-1]
            game_col_let_nber = row_letters_number[i-1]
    return (game_board, game_col_let_nber)


def advanced_settings(game_size):

    """
    The function uses game_size as argument and set 
    the number of battleships allowed or required.  
    """

    if game_size == "1":
        nber_ships = 5
        entries_col = "column (A to E for 5x5):"
        entries_row = "row (1 to 5):"
        cols_index = ['A', 'B', 'C', 'D', 'E']
        rs_index = ['1', '2', '3', '4', '5']
    elif game_size == "2":
        nber_ships = 10
        entries_col = "column (A to E for 10x10):"
        entries_row = "row (1 to 10):"
        cols_index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        rs_index = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    elif game_size == "3":
        nber_ships = 20
        entries_col = "column (A to T for 20x20):"
        entries_row = "row (1 to 20):"
        cols_index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
            'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
        rs_index = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
            '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    else:
        pass

    return (nber_ships, entries_col, entries_row, cols_index, rs_index)


def battleships_def_pos(game_size, game_col_conv, game_board):

    """
    the function will be used to determine if the battleship
    positions is chosing by a computer of the second players.
    If only one player, he would have to play with the computer.
    if 2 players, players 1 will enter the positions of the
    battleships and the players 2 will have to play the game.
    """

    print("How to choose the battleships positions?")
    print("\n"*2)
    print("Please choose 1 if a friend should do it \n")
    print("          or  2 if automatically generated by the game \n")

    while True:
        nber_player = input("Enter your choice here:")
        if nber_player not in ["1", "2"]:
            print("your choice is wrong! Pick a number between 1 et 2")
        else:
            break

    if nber_player == "1":
        data_list_of_list = user_place_battleship(game_size, game_col_conv, game_board)
    elif nber_player == "2":
        data_list_of_list = computer_place_battleship(game_size, game_col_conv, game_board)
    else:
        pass

    return data_list_of_list


def user_place_battleship(game_size, game_col_conv, game_board):

    """
    The function allows the player to enter the hidden Battleships in the game board.
    An error exception raise if the user enter the same position  more than one time.
    """

    nber_ships, entries_col, entries_row, cols_index,rs_index = advanced_settings(game_size)    
    row_number_list = []
    column_number_list = []
    for n in range(nber_ships):
        while True:
            print("Where do you want ship ", n + 1, "?")
            column = input(f"{entries_col}").upper()
            row = input(f"{entries_row}")
            if validate_battleships_positions_letter(nber_ships, column) and validate_battleships_positions_number(nber_ships, row) and validate_battleships_positions_number_0(nber_ships, row):
                print("valid entries")
                column_number = game_col_conv[column]
                row_number = int(row) - 1
                if already_used_position(game_board, row_number, column_number):
                    game_board[row_number][column_number] = 'X'
                    row_number_list.append(row_number)
                    column_number_list.append(column)
                    break

    data_list_of_list = record_ships_pos(row_number_list, column_number_list)
     
    df = pd.DataFrame(game_board, columns=cols_index)
    df.index = rs_index
    print(df)
    print("\n"*1)
    print("Legends")    
    print(" '_' : empty positions")
    print(" 'X' : positions of the Battleships")    
    print("\n"*1)
    return data_list_of_list


def computer_place_battleship(game_size, game_col_conv, game_board):
    """
    THis function id called for automatic populated the game board with battleships.
    """
    nber_ships, entries_col, entries_row, cols_index, rs_index = advanced_settings(game_size)
    column_number_list = []
    row_number_list = []
    for n in range(nber_ships):
        while True:
            x_coord = random.randint(1, nber_ships) - 1
            y_coord = random.randint(1, nber_ships) - 1
            if already_used_position(game_board, x_coord, y_coord):
                game_board[x_coord][y_coord] = "X"
                for key, value in game_col_conv.items():
                    if y_coord == value:
                        column = key
                        column_number_list.append(column)
                row_number_list.append(x_coord)
                break

    data_list_of_list = record_ships_pos(row_number_list, column_number_list)

    df = pd.DataFrame(game_board, columns=cols_index)
    df.index = rs_index
    print(df)
    print("\n"*1) 
    print("Legends")   
    print(" '_' : empty positions")
    print(" 'X' : positions of the Battleships")    
    print("\n"*1)
    return data_list_of_list


def validate_battleships_positions_letter(nber_ships, column):

    """
    The function called an exception when the inputs letter is 
    outside the allowed limites. 
    """
    if nber_ships == 5:
        letter_span = "ABCDE"
    elif nber_ships == 10:
        letter_span = "ABCDEFGHIJ"
    else:
        letter_span = "ABCDEFGHIJKLMNOPQRST"

    try:
        if letter_span.find(column) == -1:
            raise ValueError(f"{column} is not a letter between  {letter_span}")

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def validate_battleships_positions_number_0(nber_ships, row):
    """
    The function called an exeption when a value less than 1 is entered. 
    """
    try:
        if (int(row) < 1):
            raise ValueError(f"{row} must be a number between 1 and {nber_ships}")

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def validate_battleships_positions_number(nber_ships, row):

    """
    The function called an exeption when an integer value
     is entered outside the allowed range. 
    """
    try:
        if (int(row) > int(nber_ships)):
            raise ValueError(f"{row} must be a number between 1 and {nber_ships}")

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def already_used_position(game_board, row_number, column_number):

    """
    The function is used to check is the same position is
    entered more than once
    """

    try:
        if game_board[row_number][column_number] == 'X':
            raise ValueError(f" there is a battleship already in that position")

    except ValueError as e:
        print(f" duplicate data: {e}, please try again.\n")
        return False
    return True


def validate_willing_to_play():

    """
    the function allow the game to wait untill the player 
    enters "yes". 
     The inputs are not case sensitive
    """

    start_ok = input(" type Yes to start : ")
    try:
        if not (start_ok.upper() == "YES"):
            raise ValueError("answer by 'Yes' if willing to play")
    except ValueError as e:
        print(f"Invalid entries: {e}, please try again.\n")
        return False
    return True


def record_ships_pos(number, letter):

    """
    THis is an intermadiate function,
    used to build a list for the purpuse of 
    recording the ships positions on google drive.
    """

    data = []
    data_list_of_list = []
    for i in range(len(number)):
        data_list_of_list.append([letter[i], number[i]])
        data.append(letter[i])
        data.append(number[i])
    battleships_positions.append_row(data)
    return data_list_of_list


def guessing_play(game_size, game_col_conv, game_board, battleships_positions):

    """
    The function is called when the player is ready to play. She or he has to follow 
    the instructions. Enter for example A and 1 if he thinks there is a ship hidden on the 
    position (0,0) etc..
    """

    nber_ships, entries_col, entries_row, cols_index, rs_index = advanced_settings(game_size)    
    nber_guess = 1 
    print("Are you ready to start guessing the Ships position?:")   

    while(1):
     if validate_willing_to_play():                        
        print("\n"*20)
        print("Your starting Board")
        print("Good Luck")
        print("\n"*2)
        new_board = clear_game_board(nber_ships,game_board,cols_index,rs_index)
        print("\n"*5)
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
                        new_board[row_number][column_number] = "o"
                        continue                         
                    else: 
                        print("Good Guess!")
                        new_board[row_number][column_number] = "X"  
                        nber_guess = nber_guess +1  
                        break                 
                
                print("\n"*2)
                df = pd.DataFrame(game_board, columns=cols_index)
                df.index = rs_index
                print(df)
                print("\n"*1) 
                print("Legends ...")
                print(" '_' : Position not yet played")
                print(" 'X' : Hit")
                print(" 'o' : Miss")
                print("\n"*1) 

                if (nber_guess == nber_ships + 1):
                    print("You have Won!")
                    print("END od The Game!")
                
        break


def clear_game_board(nber_ships,game_board,cols_index,rs_index):

    """
    This function display an empty starting 
    game borad
    """

    for i in range(nber_ships):
        for j in range(nber_ships):
            if game_board[i][j] == "X":
                game_board[i][j] = "_"
    
    df = pd.DataFrame(game_board, columns=cols_index)
    df.index = rs_index
    print(df)
    return game_board


def play_again():

    """
    Allow the player, et the end of the game to play again or 
    log out of the game 
    """

    print("press 'y' to play again or 'n' to end the game" )
    
    while(True):
        replay_answer = input("Enter your choice here:")
        if replay_answer not in ["y", "n"]:
            print("Please press 'y' to play again or 'n' to end the game !")
        else:
            break
    if replay_answer == "y":
        main()
    elif replay_answer == "n":     
        exit()
    else:
        pass


def main():
    game_board, game_col_conv, game_size = game_set_up()
    battleships_positions = battleships_def_pos(game_size, game_col_conv,game_board)    
    guessing_play(game_size,game_col_conv,game_board, battleships_positions)
    play_again()

    
main()
