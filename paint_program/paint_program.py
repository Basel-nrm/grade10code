"""
Name: Basel
Date: 10/23/2024
Discription: This a program that will ask the user his name, address, and contact information. Then it will ask for how many walls the user wants to paint 
it will then print the different deals for paint that the user can choose from and then, depending on what the user chooses, the program will print 
the cost of all the paint that they need and will ask for the user to choose a method of purchase. After purcasing the paint, a formatted reciept 
will be printed with all the inputed information on it.
"""
from math import ceil
import random
from utils import (read_alpha, read_positive_integer,
                    change_converter, read_integer_in_range)
from wall import Wall
from datetime import date

SQUARE_FOOTAGE_PER_GALLON = 400

paint_prices = {
     1: ["Premium Paint", 105],
     2: ["Low Odor Paint", 90], 
     3: ["Regular Paint", 75], 
     4: ["Value paint", 40]
    }

def pay_by_cash(total_after_tax: float) -> bool:
    '''    
    How much are you paying? 200
    You paid $200, so your change will be: $200 - $101.70 = $98.30
    Your change will be:
    fifties: 1
    twenties: 2
    fives: 1
    toonies: 1
    loonies: 1
    quarters: 1
    nickels: 1
    '''
    while(user_payment := float(input("How much are you paying?: "))):
        if user_payment < total_after_tax:
            print(f"You cannot pay less than {total_after_tax}")
        else:
            break
    user_change = user_payment - total_after_tax
    print(f"You paid ${user_payment} so your change will be: ${user_payment} - ${total_after_tax} = ${round(user_change, 2)}")

    change_converter(user_change) 
    return True


def pay_by_card() -> bool:
    user_input = input("Please swipe your card, when done press enter")
    return True


def print_receipt(receipt_contents: dict):
    with open('./receipt.txt') as f:
        receipt = f.read()
    print(receipt.format(**receipt_contents))

# Add comments for the whole program

if __name__ == "__main__":
    # Name shouldn't except spaces or enter button
    user_name = read_alpha("What is your name?: ")

    while (True):
        # When space or enter is inputed, print "please enter something"
        temp = input("How many walls are you willing to paint? Please enter a number between 1 and 10: ")
        try:
            num_walls = int(temp)
            if (num_walls < 0):
                print("only input postitive numbers")
            elif num_walls not in range(1, 11):
                print("only input numbers between 1 and 10")
            else:
                break
            continue
        except:
            print("Only input integers, no letters, characters decimals, or nothing")

    walls = []
    for i in range (num_walls):
        # When space or enter is inputed, print "please enter something"
        wall_length = read_positive_integer(f"What is the length of your wall number {i+1} in feet?: ")
        wall_width = read_positive_integer(f"What is the width of your wall number {i+1} in feet?: ")
        new_wall = Wall(wall_width, wall_length)
        walls.append(new_wall)

    total_wall_area = 0    
    for i in range(num_walls):
        wall_area = walls[i].calc_area()
        print(f"The area of wall {i+1} is {wall_area} sq ft")
        total_wall_area += wall_area
    
    print(f"The total area of all your walls is {total_wall_area} sq ft")
   
    gallons_paint = total_wall_area / SQUARE_FOOTAGE_PER_GALLON
    print(f"the amount of paint you need is {round (gallons_paint, 2)} gallons")

    print("Here are your paint options:")
    for i in range(4):
        print(f"{i+1}.) {paint_prices[i+1][0]}: ${paint_prices[i+1][1]} per gallon")
    print("5.) Exit the program")

    choice = read_integer_in_range("Choose from options 1 to 5: ", range(1, 6))
    if choice == 5: exit()

    total_before_tax = gallons_paint * paint_prices[choice][1]
    tax_amount = total_before_tax * 0.13
    total_after_tax = round(total_before_tax + tax_amount , 2)

    print(f"The total cost of your purchase will be ${round(total_before_tax, 2)} (without tax)")

    print(f"The total cost of your purchase will be ${total_after_tax } (without tax)")

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