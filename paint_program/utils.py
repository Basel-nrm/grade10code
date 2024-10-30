def read_alpha(prompt: str) -> str:
    # while (True):
       # alpha = str(input(prompt)).replace(" ","")
    while (alpha := str(input(prompt)).replace(" ","")):
        count1 = 0
        count2 = 0
        for i in range (len(alpha)):
            try:
                int(alpha[i])
                count1 += 1
            except:
                if not alpha [i].isalpha():
                    count2 += 1
        if count1 > 0 and count2 == 0:
            print("No numbers, only letters")
        elif count1 == 0 and count2 > 0:
            print("No symbols, only letters")
        elif count1 > 0 and count2 > 0:
            print("No symbols or numbers, only letters")
        elif alpha == " ":
            print("Enter something")
        else:
            alpha2 = alpha
            break
    return alpha
    
def read_positive_integer(prompt: str) -> int:
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