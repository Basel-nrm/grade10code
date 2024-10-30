"""
Name: Basel
Date: 10/23/2024
Discription: This a program that will ask the user his name, address, and contact information. Then it will ask for how many walls the user wants to paint 
it will then print the different deals for paint that the user can choose from and then, depending on what the user chooses, the program will print 
the cost of all the paint that they need and will ask for the user to choose a method of purchase. After purcasing the paint, a formatted reciept 
will be printed with all the inputed information on it.
"""

from utils import read_alpha, read_positive_integer
from wall import Wall

SQUARE_FOOTAGE_PER_GALLON = 400

paint_prices = {
     1: ["Premium Paint", 105],
     2: ["Low Odor Paint", 90], 
     3: ["Regular Paint", 75], 
     4: ["Value paint", 40]
    }

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

    choice = int(input("Choose from options 1 to 5: ")) # add error handling
    if choice == 5: exit()

    total_before_tax = gallons_paint * paint_prices[choice][1]
   
    total_after_tax = round(total_before_tax * 1.13 , 2)

    print(f"The total cost of your purchase will be ${round(total_before_tax, 2)} (without tax)")

    print(f"The total cost of your purchase will be ${total_after_tax } (without tax)")

    print(
        "How are you paying? \n",
        "1.) Cash \n",
        "2.) Debit/Credit \n",
        "3.) Exit the program"
        )
    choice2 = int(input("Choose from options 1 to 3: ")) # add error handling
    if choice == 3: exit()
    if choice == 1: get_change()
    print_receipt()
'''
Choose from options 1 to 5: 2
The total cost of your purchase will be $90 x 1 = $90 (no tax)
The total cost of your purchase with will be $101.70 (with tax)
How are you paying:
1.) Cash
2.) Debit/Credit
3.) Exit the program
Choose from options 1 to 3: 1
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
Your receipt:
*****************************************************
SIR MIXALOT PAINT
5353 Fake street, Burlington ON, N4C 4M2
invoice #: 314554
Receiver Name: Mr. Bawa
Date: Oct, 17, 2024
Description:` Low Odor Paint
Quantity: 1
Price per gallon: $90
Subtotal: $90
Tax (13%): $11.70
Total: 101.70
Balance Due: $0.00
Thank you for your business!
****************************************************
'''