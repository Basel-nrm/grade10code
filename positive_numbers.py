def calculate_operations(num1, num2):
    # Perform calculations
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    quotient_result = num1 / num2 if num2 != 0 else "Undefined (division by zero)"
    
    return sum_result, difference_result, product_result, quotient_result

def main():
    # Get user input
    try:
        num1 = float(input("Enter the first positive number: "))
        num2 = float(input("Enter the second positive number: "))

        # Check if numbers are positive
        if num1 <= 0 or num2 <= 0:
            print("Both numbers must be positive.")
            return

        # Calculate results
        results = calculate_operations(num1, num2)

        # Print results
        print(f"Sum: {results[0]}")
        print(f"Difference: {results[1]}")
        print(f"Product: {results[2]}")
        print(f"Quotient: {results[3]}")

    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
