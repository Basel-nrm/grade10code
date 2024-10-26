
def read_int(a_list: list) -> list:
    '''
    Reads two integers and appends them to input list

    Args:
        a_list (list): The given list.

    Returns:
        list: The resulting list from appending the two integers to the given list
    '''
    counter = 1
    while (counter <= 2):
        try:
            integer1 = int(input("Please enter an integer: "))
        except:
            continue
        a_list += [integer1]
        counter += 1
    return a_list

def read_decimal(a_list: list) -> list:

    '''
    reads two decimals and appends them to input list

    Args:
        a_list (list): the given list

    Returns:
        list: The resulting list from appending the two decimals to the given list
    '''
    counter = 1
    while (counter <= 2):
        try:
            decimal1 = float(input("Please enter a decimal: "))
        except:
            continue
        a_list += [decimal1]
        counter += 1
    return a_list


if __name__ == "__main__":
    # Calling functions to read values and add them to the list
    my_list = []
    my_list = read_int(my_list)
    my_list = read_decimal(my_list)

    # Asking for two strings and storing them in the list
    text1 = str(input("Please enter your name: "))
    my_list += [text1]
    text2 = str(input("Please enter your favourite food: "))
    my_list += [text2]
    
    # Printing the radom sentences
    print(f"The sum of {my_list[0]} and {my_list[1]} is {my_list[0] + my_list[1]}")
    print(f"The product of {my_list[2]} and {my_list[3]} is {my_list[2] * my_list[3]}")
    print(f"Your name is {my_list[4]} and your favourite food is {my_list[5]}")