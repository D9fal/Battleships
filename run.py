# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

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
    print("setting up the game ... \n")
    print("Please enter 1 for 5X5   game size \n")
    print("       enter 2 for 10X10 game size \n")
    print("       enter 3 for 20X20 game size \n")

    game_size = input("Enter your choice here:")
    
def drawing_game():

def main():
    game_set_up()

main()