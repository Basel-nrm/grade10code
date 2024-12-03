'''
11/21/2024
Basel Mabroukeh
This is a tic tac toe game program. This program creates a tic tac toe board and then asks the user which cell they wish to
put an X or an O in. The program then keeps reading the board until it finds a player who has gotten 3 X's or O's in a row 
and labels them as the winner.
'''

#prints the sample board
def sampleBoard():
    '''
    Creates and prints a sample board to show the number of each cell.
    '''
    print("\n1 | 2 | 3")
    print("----------")
    print("4 | 5 | 6")
    print("----------")
    print("7 | 8 | 9\n\n")

def printBoard(board: list):
    '''
    Args:
        board (list): Prints the tic tac toe board layout.

    '''
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def playerInput(board: list):
    '''
    Allows the player1 & player2 to input into a spot
    Args:
        board (list): The tic tac toe board layout.
    '''
    global turns, player1, player2
    player1 = "\033[31mX\033[0m"
    player2 = "\033[34mO\033[0m"
    while True:
        choice1 = str(input("\nEnter a number between 1 & 9: "))
        try:
            choice = int(choice1)
            if choice >= 1 and choice <= 9 and board[choice-1]== "-":
                if turns % 2 == 0:
                    board[choice - 1] = player1
                    turns += 1
                    break
                else:
                    board[choice - 1] = player2
                    turns += 1
                    break
            elif choice > 9 or choice <= 0:
                print("\nOnly input values between 1 and 9")
            else:
                print("\nSpot has already been occupied\n")
        except:
            print("Only integer input")

def checkHorizontal(board: list):
    '''
    Checks to see if there is a winner horizontally
    Args:
        board (list): The tic tac toe board layout.
    '''
    global winner
    if board[0] == board[1] == board[2] and board[0]!= "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3]!= "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6]!= "-":
        winner = board[6]
        return True

def checkVertical(board: list):
    '''
    Checks to see if there is a winner vertically
    Args:
        board (list): The tic tac toe board layout.
    '''
    global winner
    if board[0] == board[3] == board[6] and board[0]!= "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1]!= "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2]!= "-":
        winner = board[2]
        return True

def checkDiagonal(board: list):
    '''
    Checks to see if there is a winner vertically
    Args:
        board (list): The tic tac toe board layout.
    '''
    global winner
    if board[0] == board[4] == board[8] and board[0]!= "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2]!= "-":
        winner = board[2]
        return True

def checkTie():
    '''
    Checks to see if nobody wins and there is a tie
    '''
    global gameRunning
    if turns == 9 and not checkDiagonal(board) and not checkVertical(board) and not checkHorizontal(board):
        printBoard(board)
        print("Its a tie!")
        gameRunning = False

def checkWin():
    '''
    Checks the diagonals, verticals and horizontals to see if there is a win
    '''
    global gameRunning
    if checkHorizontal(board) or checkVertical(board) or checkDiagonal(board):
        printBoard(board)
        print(f"The winner is {winner}")
        gameRunning = False

def tictactoe():
    '''
    This is the loop that will run the game
    '''
    global board, gameRunning, winner, turns
    #this is a 1D list/arry for the board
    board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

    #initializes variables to start the game
    gameRunning = True
    winner = ""
    turns = 0
    while gameRunning:
        sampleBoard()
        printBoard(board)
        playerInput(board)
        checkWin()
        checkTie()
        if gameRunning == False:
            while True:
                print("Would you like to play again, y or n")
                answer = str(input()).lower()
                if answer == "n":
                    print("Thanks for playing")
                    break
                elif answer == "y":
                    board = ["-","-","-",
                        "-","-","-",
                        "-","-","-"]
                    gameRunning = True
                    winner = ""
                    turns = 0
                    break
                else:
                    print("Only type y or n")