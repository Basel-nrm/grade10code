'''
11/21/2024
Basel Mabroukeh
TODO: add descrption here
'''
# TODO: isntead of multiple sentences containing info on player 1 and two, make a formatted block of info for each player e.g: 
# player 1          player 2
# score: 1          score:1
# answer: rock      answer: rock

import random
import numpy as np
from utils2 import read_integer_in_range, play_again, clearscreen


# look up table of answers, the list next to each answer represents what looses to that answer
# for example scissors looses to rock so 3 is in the list of loosers for answer 1
answers = {1:('rock', [3]),
        2:('paper', [1]), 
        3:('scissors', [2])}

def determine_winner(player1_answer: int, player2_answer: int) -> list[int, int]:
    print("Player 1 answer is ", answers[player1_answer][0])
    print("Player 2 answer is ", answers[player2_answer][0])
    if player1_answer == player2_answer: 
        print("It's a tie, you both score!")
        return [1,1]
    if player2_answer in answers[player1_answer][1]:
        print("Player 1 wins !")
        return [1,0]
    print("Player 2 wins !")
    return [0,1]

def rps():

    #initializes the scores when program is called
    while True:
        print("""\t\t Welcome to RPS
            1.) 1 player option
            2.) 2 player option
            3.) return to the main menu
        """)
        choice = read_integer_in_range("choose an option from 1 to 3: ", range(1, 4))
        if choice == 3: return
        scores = [0, 0]
        while True:
            player1_answer = read_integer_in_range("\033[31mPlayer 1\033[0m, Type 1 for rock, 2 for paper or 3 for scissors: ", range(1, 4))
            clearscreen()
            player2_answer = 0
            if choice == 1:
                print("\033[31mPlayer 2\033[0m is computer")
                player2_answer = random.randint(1, 3)
            if choice == 2:
                player2_answer = read_integer_in_range("\033[31mPlayer 2\033[0m, Type 1 for rock, 2 for paper or 3 for scissors: ", range(1, 4))
            score_increments = determine_winner(player1_answer, player2_answer)
            scores = np.array(scores) + np.array(score_increments)  # array addition 
            print(f"Player 1 score: {scores[0]}\nPlayer 2 score: {scores[1]}")
            if not play_again(): break