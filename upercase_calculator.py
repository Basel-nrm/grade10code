def count_case_letters(input_string):
    uppercase_count = 0
    lowercase_count = 0
    
    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
            
    return uppercase_count, lowercase_count

def main():
    # Get user input
    input_string = input("Enter a string: ")

    # Calculate counts
    uppercase_count, lowercase_count = count_case_letters(input_string)

    # Print results
    print(f"Uppercase letters: {uppercase_count}")
    print(f"Lowercase letters: {lowercase_count}")

if __name__ == "__main__":
    main()
