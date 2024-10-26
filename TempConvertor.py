'''
Oct, 9, 2024
Basel Mabroukeh
This is the program for question 2 of Programming Excercises part 2
'''

def print_header(choice: int):
    if choice == 1:
        print("C , F")
    if choice == 2:
        print("F , C")

def convert(start_val: int, choice: int) -> float:
    result = 0
    if choice == 1:
        result = (9 / 5 * start_val) + 32
    if choice == 2:
        result = (start_val - 32) * 5 / 9
    return result


if __name__ == "__main__":
    while (True):
        try:
            choice = int(input("Type 1 to convert from C to F or 2 to convert from F to C: "))
            if choice not in [1, 2]: continue
                
            start_val = int(input("Please input a starting value in celsius: "))
            end_val = int(input("Please input a ending value in celsius: "))
            break
        except:
            print("please enter only numeric values \n")

    print_header(choice)
    for i in range(start_val, end_val + 1):
        print(start_val, round(convert(start_val, choice), 2))
        start_val += 1
        


    
