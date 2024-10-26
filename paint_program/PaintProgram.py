"""
Basel
10/23/2024
This a program that will ask the user his name, address, and contact information. Then it will ask for how many walls the user wants to paint 
it will then print the different deals for paint that the user can choose from and then, depending on what the user chooses, the program will print 
the cost of all the paint that they need and will ask for the user to choose a method of purchase. After purcasing the paint, a formatted reciept 
will be printed with all the inputed information on it.
"""

from utils import read_alpha, read_positive_integer
from wall import Wall


if __name__ == "__main__":
   # learn regex, logical expressions, classes and methods, version control





   
    while (True):
        name = str(input("What is your name?: ")).replace(" ","")
        count1 = 0
        count2 = 0
        for i in range (len(name)):
            try:
                int(name[i])
                count1 += 1
            except:
                if not name [i].isalpha():
                    count2 += 1
        if count1 > 0 and count2 == 0:
            print("No numbers, only letters")
        elif count1 == 0 and count2 > 0:
            print("No symbols, only letters")
        elif count1 > 0 and count2 > 0:
            print("No symbols or numbers, only letters")
        elif name == "":
            print("Enter something")
        else:
            name2 = name
            break
    
    while (True):
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
            print("Only input integers, no letters, characters or decimals")

    num1 = []
    for i in range (num_walls):
        while (True):
            try:
                wall_length = int(input(f"What is the length of your wall number {i+1} in feet?: "))
                if (wall_length <= 0):
                    print("only input postitive numbers")
                else:
                    break
            except:
                print("Only input integers, no letters, characters or decimals")
        while (True):
            try:
                wall_width = int(input(f"What is the width of your number {i+1} wall in feet?: "))
                if (wall_width <= 0):
                    print("only input postitive numbers")
                else:
                    break
                continue
            except:
                print("Only input integers, no letters, characters or decimals")