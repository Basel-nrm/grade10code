nums = [200, 100]
words = ["Fifties", "Twenties", "Tens", "Fives", "Toonies", "Loonies", "Quarters", "Dimes", "Nickels", "Pennies"]
change1 = float(input("Please enter a dollar amount between $0 and $100: "))
change2 = int(change1*100)
print ("Here is your change")
for i in range(0, 10):
    print(words[i], change2//nums[i])
    change2 %= nums [i]
