'''
Oct, 9, 2024
Basel Mabroukeh
This is the program for question 3 of Programming Excercises part 2
'''

if __name__ == "__main__":
    nums = [5000, 2000, 1000, 500, 200, 100, 25, 10, 5, 1]
    words =  ["Fifties", "Twenties", "Tens", "Fives", "Toonies", "Loonies", "Quarters", "Dimes", "Nickels", "Pennies"]
    while (True):
        try:
            change1 = float(input("Please enter a dollar amount between $0 and $100: "))
            if change1 < 0: continue
            break
        except:
            print("please input only numerical real numbers")
            
    change2 = int(change1*100)
    print ("Here is your change")
    for i in range(0, 10):
        val = change2 // nums[i]
        change2 %= nums[i]
        if val == 0: continue
        print(words[i], val)
    
        
        
    
