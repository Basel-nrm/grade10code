'''
11/21/2024
Basel Mabroukeh
TODO: add descrption here
'''

import time

def loading():
    print("loading", end="")
    for i in range(0, 4):
        print(".", end="")
        time.sleep(1)

def clearscreen():
    for i in range(0, 30):
        print("\n")

while True:
    a = '🤩'
    print("\t ",a, a, a, a, a, a, a, a, a, a, a)
    print("""\t Welcome to Bawa Mini Games
        1.) RPS
        2.) High Low Guessing Game
        3.) Tic Tac Toe
        4.) Exit
        Choose one of the following options
    """)
    print("\t ",a, a, a, a, a, a, a, a, a, a, a)
    choice = str(input())
    if choice == "1":
        loading()
        clearscreen()
        rps()
    elif choice == "2":
        loading()
        clearscreen()
        highlow()
    elif choice == "3":
        loading()
        clearscreen()
        tictactoe()
    elif choice == "4":
        loading()
        clearscreen()
        print("Thank you for using my program")
        exit()
    else:
        clearscreen()
        print("Enter 1 to 4 only please!")
