
# Function to find the row with the most number of 1's
def row_with_most_ones(binary_matrix):
    max_ones = 0
    row_index = -1
    
    # Iterate over each row and count the number of 1's
    for i in range(len(binary_matrix)):
        ones_count = binary_matrix[i].count(1)
        if ones_count > max_ones:
            max_ones = ones_count
            row_index = i
    
    return row_index, max_ones


if __name__ == "__main__":
    # Example binary matrix (2D array)
    binary_matrix = [
        [0, 1, 1, 0, 1],
        [1, 1, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 0, 0, 1]
    ]

    # Find the row with the most 1's
    row_index, max_ones = row_with_most_ones(binary_matrix)

    # Output the result
    if row_index != -1:
        print(f"Row {row_index + 1} has the most 1's with a total of {max_ones}.")
    else:
        print("No 1's found in the matrix.")