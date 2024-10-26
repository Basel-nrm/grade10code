def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def main():
    numbers = []
    
    print("Please enter 5 numbers:")
    
    for i in range(5):
        while True:
            try:
                num = float(input(f"Number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    # Calculate average
    average = calculate_average(numbers)

    # Print the result
    print(f"The average of the entered numbers is: {average}")

if __name__ == "__main__":
    main()