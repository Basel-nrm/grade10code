"""
Name: Basel
Date: 10/23/2024
Discription: This a program that will ask the user his name, address, and contact information. 
Then it will ask for how many walls the user wants to paint it will then print the different deals
for paint that the user can choose from and then, depending on what the user chooses, the program
will print the cost of all the paint that they need and will ask for the user to choose a method 
of purchase. After purcasing the paint, a formatted reciept will be printed with all the inputed
information on it.
"""
# Importing required packages and classes
from math import ceil
import random
from utils import (read_alpha, read_positive_integer,
                    change_converter, read_integer_in_range)
from wall import Wall  # see definition of Wall class in wall.py
from datetime import date

# defining a constant
SQUARE_FOOTAGE_PER_GALLON = 400

# Creating a dictionary to use later in the program
paint_prices = {
     1: ["Premium Paint", 105],
     2: ["Low Odor Paint", 90], 
     3: ["Regular Paint", 75], 
     4: ["Value paint", 40]
    }

def pay_by_cash(total_after_tax: float) -> None:
    '''
    This function asks the user for payment if the user chose to pay by cash
    Args:
        total_after_tax: float value of the total price after tax
    Return
        none
    '''
    # using the new Walrus operator https://peps.python.org/pep-0572/ 
    while(user_payment := float(input("How much are you paying?: "))):
        if user_payment < total_after_tax:
            print(f"You cannot pay less than {total_after_tax}")
        else:
            break
    user_change = user_payment - total_after_tax
    print(f"You paid ${user_payment} so your change will be: ${user_payment} - ${total_after_tax} = ${round(user_change, 2)}")
    # now print the change in words
    change_converter(user_change) 

def pay_by_card() -> None:
    ''' 
    A function that asks the user to continue after swiping their card 
    if the user chose to pay by card 
    Args:
        none
    Returns:
        none
    '''
    user_input = input("Please swipe your card, when done press enter")

def print_receipt(receipt_contents: dict) -> None:
    '''
    A function that prints the reciept
    Args:
        receipt_contents (dict): All the values to populate the receipt template
    Returns:
        N/A
    '''
    # I created a receipt template in receipt.txt
    with open('./receipt.txt') as f: # Reads the receipt template
        receipt = f.read()
    # Using the dictionary to fill the template with appropriate values
    print(receipt.format(**receipt_contents)) 


if __name__ == "__main__":

    user_name = read_alpha("What is your name?: ")
 
    # call a function to ask the user to input how many walls they want to paint with error handling
    num_walls = read_integer_in_range("How many walls are you willing to paint? Please enter a number between 1 and 10: ", range(1, 11))
 
    # Asking user to input the length and width of each wall and storing all the values into a list of wall objects
    walls = []
    for i in range (num_walls):
        wall_length = read_positive_integer(f"What is the length of your wall number {i+1} in feet?: ")
        wall_width = read_positive_integer(f"What is the width of your wall number {i+1} in feet?: ")
        new_wall = Wall(wall_width, wall_length)
        walls.append(new_wall)

    # Calculating the total wall area of all the walls combined
    total_wall_area = 0    
    for i in range(num_walls):
        wall_area = walls[i].calc_area()  # using a method in the Wall class
        print(f"The area of wall {i+1} is {wall_area} sq ft")
        total_wall_area += wall_area
    
    # Printing the total wall area
    print(f"The total area of all your walls is {total_wall_area} sq ft")
   
    # Calculating how much paint the user will need and printing the amount
    gallons_paint = total_wall_area / SQUARE_FOOTAGE_PER_GALLON
    print(f"the amount of paint you need is {round (gallons_paint, 2)} gallons")

    # using the paint_prices dictionary to print and display all the paint options
    print("Here are your paint options:")
    for i in range(4):
        print(f"{i+1}.) {paint_prices[i+1][0]}: ${paint_prices[i+1][1]} per gallon")
    print("5.) Exit the program")

    # Proccessing the users input to select the option they chose
    choice = read_integer_in_range("Choose from options 1 to 5: ", range(1, 6))
    if choice == 5: exit()

    # Calculating the total cost of the paint that the user is buying with and without tax
    total_before_tax = gallons_paint * paint_prices[choice][1]
    tax_amount = total_before_tax * 0.13
    total_after_tax = round(total_before_tax + tax_amount , 2)

    # Printing the total cost of the paint before and after tax
    print(f"The total cost of your purchase will be ${round(total_before_tax, 2)} (without tax)")
    print(f"The total cost of your purchase will be ${total_after_tax } (without tax)")

    # Printing the options of payment and reading the user's choice 
    print(
        "How are you paying? \n",
        "1.) Cash \n",
        "2.) Debit/Credit \n",
        "3.) Exit the program"
        )
    choice2 =  read_integer_in_range("Choose from options 1 to 3: ", range(1, 4))
    if choice2 == 3: exit()
    if choice2 == 1: pay_by_cash(total_after_tax)
    if choice2 == 2: pay_by_card()

    # Printing a pre-formatted reciept
    print_receipt(
        {
            'random_num': random.randint(1, 1000000),
            'name': user_name,
            'date_val': date.today(),
            'paint_type': paint_prices[choice][0],
            'qty': ceil(gallons_paint),
            'paint_price': paint_prices[choice][1],
            'total_before_tax': round(total_before_tax, 2),
            'tax_amount': round(tax_amount, 2),
            'total_after_tax': total_after_tax
        }
    )