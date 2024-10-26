
def get_integers():
    integers = []
    while len(integers) < 10:
        try:
            num = int(input(f"Enter integer {len(integers) + 1} of 10: "))
            integers.append(num)
        except ValueError:
            print("Invalid input. Please enter an integer.")
    return integers

def main():
    print("Please enter 10 random integers.")
    integers = get_integers()
    
    # Sort the array
    integers.sort()
    
    # Print forwards
    print("Sorted array (forwards):", integers)
    
    # Print backwards
    print("Sorted array (backwards):", integers[::-1])

if __name__ == "__main__":
    main()