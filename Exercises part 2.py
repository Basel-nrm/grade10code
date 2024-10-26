'''
Oct, 8, 2024
Basel Mabroukeh
This is the program for question 1 of Programming Excercises part 2
'''
if __name__ == "__main__":
    # Reading and checking input (error handling)
    while True:
        num1 = str(input("Please enter a 5 digit number "))  
        try:
            num = int(num1) 
            if num < 0:  
                print("only postive numbers")
            else:
                if len(num1) != 5:  
                    print("Input a 5 digit number only!")
                else:
                    break
        except:
            print("only integer numbers, no letters, characters or decimals")
    # Using integer division to seperate the digits in the 5 digit number
    divisor = 10000
    val_list = []
    for i in range(1, 6): 
        val = int(num / divisor)
        rem = int(num % divisor)
        val_list.append(val)
        num = rem
        divisor /= 10
    print(val_list)

