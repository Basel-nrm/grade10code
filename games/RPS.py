'''
11/21/2024
Basel Mabroukeh
This is a rock, paper, scissors, game program that asks the user if the want to play against the computer or if they want to play
against another player. It then aks the user to input 1 for rock, 2 for paper, and 3 for scissors and then compares the player's answer
to the computer or other player's answer and determines who the winner is while printing out both of the player's information.
'''

import random
import numpy as np
from utils2 import read_integer_in_range, play_again, clearscreen


# A look up table of answers, the list next to each answer represents what looses to that answer
# For example scissors looses to rock so 3 is in the list of loosers for answer 1
answers = {1:('rock', [3]),
        2:('paper', [1]), 
        3:('scissors', [2])}

def determine_winner(player1_answer: int, player2_answer: int) -> list[int, int]:
    '''
    Determines who is winning any given round by comparing the answers of each player.
    Args:
        player1_answer (int): First player's answer as an integer code as shown in the 'answers' dictionary.
        player2_answer (int): Second player's answer as an integer code as shown in the 'answers' dictionary.
    Returns:
        list [int, int]: A list representing the score for both players in the given round
    '''    
    if player1_answer == player2_answer: 
        print("\nIt's a tie, you both score!")
        return [1,1]
    if player2_answer in answers[player1_answer][1]:
        print("\nPlayer 1 wins this round!")
        return [1,0]
    print("\nPlayer 2 wins this round!")
    return [0,1]

def print_score_board(scores: list, p1answer: int, p2answer:int):
    '''
    Prints the information about both players depending in any given round.
    Args:
        scores (list): A list representing the score for both players in the given round
        p1answer (int): The answer the first player chose
        p2answer (int): The answer the second player chose
    '''
    print(f'''
    player 1\t\tplayer 2
    --------\t\t--------
    score: {scores[0]}\t\tscore:{scores[1]}
    answer: {answers[p1answer][0]}\tanswer: {answers[p2answer][0]}
    ''')
   
def rps():
    '''
    This is the loop that will run the game.
    '''
    #initializes the scores when program is called
    while True:
        clearscreen()
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
            scores = np.array(scores) + np.array(score_increments)  # array addition, ref: https://stackoverflow.com/questions/58090632/numpy-add-with-multiple-arrays
            print_score_board(scores, player1_answer, player2_answer)
            if not play_again(): break
