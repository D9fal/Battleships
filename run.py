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

computer_generated_positions = SHEET.worksheet('computer')
player1_data = SHEET.worksheet('player1')
player2_data = SHEET.worksheet('player2')

ships_positions = computer_generated_positions.get_all_values()
player1_d = player1_data.get_all_values()
player2_d = player2_data.get_all_values()

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
            'k': 10,
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
            game_row_let_nber = row_letters_number[i-1]
    return (game_board, game_row_let_nber)    


def number_player(game_size, game_row_conv, game_board):
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
        player_place_battleship(game_size, game_row_conv, game_board)
    elif nber_player == "2":
        computer_place_battleship(game_size, game_row_conv, game_board)
    else:
        pass

def player_place_battleship(game_size, game_row_conv, game_board):
    """ 
    """
    if game_size == "1":
        nber_ships = 5 
    elif  game_size == "2":
        nber_ships = 10
    elif game_size == "3":
        nber_ships = 10
    else: 
        pass

    for n in range(nber_ships):

        print("Where do you want ship ", n + 1, "?")
        column = input("column (A to E for 5x5) - column (A to J for 10x10) - column(A to T for 20x20):")
        row = input("row (1 to 5) - row (1 to 10) - row (1 to 20):")        
        column_number = game_row_conv[column]        
        row_number = int(row) - 1
        game_board[row_number][column_number] = 'X'   
    for row in game_board:
        print(row)    




def computer_place_battleship(game_size, game_row_conv, game_board):
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
    
    for n in range(nber_ships): 
         
        game_board[random.randint(0,nber_ships)-1][random.randint(0,nber_ships)-1] = "X"
    
    for row in game_board:
        print(row)    


def main():
    game_board, game_row_conv, game_size = game_set_up()
    number_player(game_size, game_row_conv,game_board)    
    
main()