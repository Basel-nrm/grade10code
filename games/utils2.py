'''
11/21/2024
Basel Mabroukeh
This is a utility library for generic functions.
'''

import os 

def clearscreen():
    '''
    Clears the screen based on the operating system.
    '''
    os.system("cls")  # ref: https://www.geeksforgeeks.org/clear-screen-python/

def read_integer_in_range(prompt: str, num_range: range) -> int:
    '''
    Reads user input as an integer in a given range
    Args:
        prompt (str): A message to prompt the user
        num_range (range): The range that the number should be in
    Returns:
        An integer within the given range
    '''
    while (True):
        try:
            num = int(input(prompt))
            if num in num_range: break 
            else:
                print(f"Number should be in the range {num_range.start} - {num_range.stop-1}")
            continue
        except:
            print("Only input integers, no letters, characters or decimals")
    return num

def play_again() -> bool:
    '''
    Asks user if they want to play again, if user inputs anything that starts
    with the letter Y it is considered a positive answer otherwise it is considered
    as a negative answer
    '''
    while True:
        answer = str(input("Do you want to play again (y/n)? ")).lower()
        if answer == "n":
            print("Thanks for playing")
            return False
        elif answer == "y":
            return True
        else:
            print("Only type y or n")