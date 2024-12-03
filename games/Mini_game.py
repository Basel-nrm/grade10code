'''
11/21/2024
Basel Mabroukeh
This program displays a list of games and asks you to input a number based on the game you would like to play 
or if you wish to exit the program. It then reads your input and sends you to the game you have chosen.
'''

import time
from tic_tac_toe import *
from utils2 import *
from RPS import rps
from highlow_guessing_game import highlow


if __name__ == "__main__":

    # Displays all the options of games that you may choose.
    while True:
        a = '💎'
        clearscreen()
        print("\t ",a, a, a, a, a, a, a, a, a, a, a)
        print("""\t Welcome to Basel Mini Games
            1.) RPS
            2.) High Low Guessing Game
            3.) Tic Tac Toe
            4.) Exit
            Choose one of the following options
        """)
        print("\t ",a, a, a, a, a, a, a, a, a, a, a)
        # Asks for an input and sends you to the game you have chosen based on your input.
        choice = str(input("Please choose from options 1 to 4: "))
        clearscreen()
        if choice == "1":
            rps()
        elif choice == "2":
            highlow()
        elif choice == "3":
            tictactoe()
        elif choice == "4":
            print("Thank you for using my program")
            exit()
        else:
            print("Enter 1 to 4 only please!")
            time.sleep(2)  # ref: https://stackoverflow.com/questions/510348/how-do-i-make-a-time-delay

