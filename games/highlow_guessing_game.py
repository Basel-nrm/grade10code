import random
from utils2 import play_again, read_integer_in_range

# TODO: add an error statement if the users input is not within the right range and clear screen if choice is play again 
# and again after exiting the game and going to the main menu
def highlow():

    while True:
        diff_lvl = read_integer_in_range("Choose difficulty by inputing 1 for \033[32measy\033[0m, 2 for \033[33mmedium\033[0m, and 3 for \033[31mhard\033[0m: ", range(1, 4))
        if diff_lvl == 1:
            print("You have chosen \033[32measy\033[0m difficlty")
            max_range = 20
            max_attempts = 10
        elif diff_lvl == 2:
            print("You have chosen \033[33mmedium\033[0m difficlty")
            max_range = 100
            max_attempts = 5
        elif diff_lvl == 3:
            print("You have chosen \033[31mhard\033[0m difficlty")
            max_range = 1000
            max_attempts = 3
        
        print(f"Welcome to Basel's high low guessing game!\n\nYou have a total of {max_attempts} guesses!\n")

        rand_num = random.randrange(1, max_range)
        # TODO: remove print rand_num
        print(rand_num)
        guess = read_integer_in_range(f"Please guess a number between 1 - {max_range}: ", range(1, max_range + 1))
        print(guess)

        attempts = 1
        while (guess != rand_num) and (attempts < max_attempts):
            if guess < rand_num:
                print("Your guess is lower than the number!")
            elif guess > rand_num: 
                print("Your guess is higher than the number!")
            guess = read_integer_in_range("Please guess again: ", range(1, max_range + 1))
            attempts += 1

        
        if guess == rand_num:
            print(f"The number was {rand_num}. You have guessed the number!")
        else:
            print("You have reached the maximum number of guesses")
        if not play_again(): break