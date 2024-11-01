import re

def read_alpha(prompt: str) -> str:
    '''
    Reads user input as a name
    Args:
        prompt (str): A message to prompt the user
    Returns:
        A name as a string
    '''
    while(True):
        alpha = str(input(prompt))
        # check if input is empty
        if len(alpha) == 0: continue
        # make sure the input name does not contain numbers or special characters or starts with a space
        # to do this I will check against a regex
        if re.search("^[^-\\s\\d][a-zA-Z\\s-]+$", alpha): break
    return alpha
 
# Error handling any posititve number input
def read_positive_integer(prompt: str) -> int:
    '''
    Reads user input as a positive integer
    Args:
        prompt (str): A message to prompt the user
    Returns:
        A positive integer
        '''
    while (True):
        try:
            num = int(input(prompt))
            if (num <= 0):
                print("only input postitive numbers")
            else:
                break
            continue
        except:
            print("Only input integers, no letters, characters or decimals")
    return num

# TODO: figure out what this does
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
            continue
        except:
            print("Only input integers, no letters, characters or decimals")
    return num

def change_converter(change_due: float) -> None:
    '''
    Breaks down a monetary number into its Canadian money components in English
     Args:
        change_due (float): The monetary number
    Returns:
        N/A       
    '''
    nums = [10000, 5000, 2000, 1000, 500, 200, 100, 25, 10, 5, 1]
    words =  ["Hundreds", "Fifties", "Twenties", "Tens", "Fives", "Toonies", "Loonies",
               "Quarters", "Dimes", "Nickels", "Pennies"]
    change2 = int(change_due*100)
    print ("Here is your change:")
    for i in range(0, 10):
        val = change2 // nums[i]
        change2 %= nums[i]
        if val == 0: continue
        print(words[i], val)

