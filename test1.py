def read_integer_in_range(prompt: str, num_range: range) -> int:
    while (True):
        try:
            num = int(input(prompt))
            #if (num < num_range[0]) or (num > num_range[1]):
            if num in num_range: break 
            continue
        except:
            print("Only input integers, no letters, characters or decimals")
    return num

x = read_positive_integer_in_range("choose option between 1 and 5: ", range (1, 6))
print(x)
