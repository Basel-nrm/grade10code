
# Initialize an empty 3x3 matrix
matrix = [[0 for _ in range(3)] for _ in range(3)]

# Input the values from the user
print("Enter numbers between 1 and 100 for the 3x3 matrix:")
for i in range(3):
    for j in range(3):
        while True:
            try:
                num = int(input(f"Enter number for position ({i},{j}): "))
                if 1 <= num <= 100:
                    matrix[i][j] = num
                    break
                else:
                    print("Please enter a number between 1 and 100.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

# Display the matrix
print("\nMatrix:")
for row in matrix:
    print(row)

# Calculate and display the sum of each row
print("\nSum of each row:")
for i in range(3): print(f"Row {i + 1}: {sum(matrix[i])}")

# Calculate and display the sum of each column
print("\nSum of each column:")
for j in range(3):
    col_sum = sum(matrix[i][j] for i in range(3))
    print(f"Column {j + 1}: {col_sum}")