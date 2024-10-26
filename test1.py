num_walls_to_paint = [1, 2, 3, 4, 5]
    
num1 = []
for i in range (0, num_walls_to_paint):
    while (True):
        try:
            walls_length = int(input("What is the length of your wall in feet?: ", i + 1 ))
            if (walls_length < 0):
                print("only input postitive numbers")
            else:
                break
            continue
        except:
            print("Only input integers, no letters, characters or decimals")

num2 = []
for i in range (0, num_walls_to_paint):
    while (True):
        try:
            walls_width = int(input("What is the width of your wall in feet?: ", i + 1))
            if (walls_width < 0):
                print("only input postitive numbers")
            else:
                break
            continue
        except:
            print("Only input integers, no letters, characters or decimals")
